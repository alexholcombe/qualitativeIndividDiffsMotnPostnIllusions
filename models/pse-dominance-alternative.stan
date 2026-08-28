
data {
  int<lower=0> N;                                  // number of data points
  int<lower=0> n_subjects;                         // number of subjects
  array[N] int<lower=1, upper=n_subjects> id;      // subject ID
  vector[N] y;                                     // response variable
  
  // model condition
  int<lower=0, upper=1> condition; // 0 = log normal, 1 = gamma
                                   
  // Prior hyperparameters
  real mean_prior_mu;
  real <lower = 0> mean_prior_sigma;       // hyperpara for prior on mean of the distribution
  real sd_prior_mu; 
  real <lower = 0> sd_prior_sigma;         // hyperpara for prior on sd of the distribution
  
  // Conditions inside data and parameter block?
  // https://mc-stan.org/docs/2_25/reference-manual/conditional-operator-section.html
  // https://discourse.mc-stan.org/t/if-else-statement-inside-parameter-block/13937/2
}

transformed data {
  int logN = condition ? 0:1;   // TRUE if condition = 0
  int gamma = condition ? 1:0;  // TRUE if condition = 1
}

parameters {
  array [1] real <offset = mean_prior_mu, multiplier = mean_prior_sigma> mean_prior_hat;
  array [1] real <offset = sd_prior_mu, multiplier = sd_prior_sigma> sd_prior_hat;
  
  vector <lower =0> [n_subjects] theta_hat;
  real <lower = 0> sigma_epsilon; 
}

transformed parameters {
  array [1] real <lower = 0> mean_prior = exp(mean_prior_hat);            // prior log normal distributed
  array [1] real <lower = 0> sd_prior = exp(sd_prior_hat);                // prior log normal distributed
  
 // reparameterization of mean and sd
 array [logN] real mu_theta;     
 array [logN] real <lower = 0> sigma_theta;
 array [gamma] real <lower = 0> alpha_theta;
 array [gamma] real <lower = 0> beta_theta;       
                                                     
 vector [ n_subjects] theta;
 
  if (logN){   // log normal
    mu_theta[logN] = log( (mean_prior[1]^2) / (sqrt(sd_prior[1]^2 + mean_prior[1]^2)) );   // transforming mean and sd into model parameters
    sigma_theta[logN] = log( (sd_prior[1]^2)/(mean_prior[1]^2) + 1 );

    theta = exp(theta_hat);
  }
  else if (gamma){ // gamma
    alpha_theta[gamma] = mean_prior[1]^2 / sd_prior[1]^2;   // transforming mean and sd into model parameters
    beta_theta[gamma] = mean_prior[1] / sd_prior[1]^2;    // transforming mean and sd into model parameters
    
    theta = theta_hat / beta_theta[gamma];
  }
}

model {
 // Priors
  target += normal_lpdf(sd_prior_hat | sd_prior_mu, sd_prior_sigma);
  target += normal_lpdf(mean_prior_hat | mean_prior_mu, mean_prior_sigma);  

 // theta conditioned on model 
  if (logN){   // log normal
    target += normal_lpdf(theta_hat | mu_theta[logN], sigma_theta[logN]);
  }
  else if (gamma) { // gamma
    target += gamma_lpdf(theta_hat | alpha_theta[gamma], 1);
  }
 
 // measurement error
  target += log(1/sigma_epsilon^2);                    // Jeffreys prior on sigma2
  
 // Likelihood
  target += normal_lpdf(y | theta[id], sigma_epsilon);
 
 
}

