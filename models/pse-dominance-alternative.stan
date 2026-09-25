
functions{
  real logN_model_lpdf(vector theta_hat, real param1, real param2){  
    return normal_lpdf(theta_hat | param1, param2);
  }
  
  real gamma_model_lpdf(vector theta_hat, real param1, real param2){  
    return gamma_lpdf(theta_hat | param1, 1);
    
  }
  
  real model_lpdf(vector theta_hat, real param1, real param2, real condition){     
    if(condition == 1) return logN_model_lpdf(theta_hat | param1, param2);         
    else if(condition == 2) return gamma_model_lpdf(theta_hat | param1, param2);
    else reject("model_lpdf: unsupported condition =", condition);
    return negative_infinity();
  }
  
  real calc_param(real m, real s, int code, real condition){
    if(code == 1) {
      if(condition == 1) return log( square(m)/sqrt(square(s) + square(m)) );
      else if(condition == 2) return square(m)/square(s);
      else reject("calc_param: unsupported condition =", condition);
      return negative_infinity();
    }
    else if(code == 2){
      if(condition == 1) return sqrt(log1p( square(s)/square(m) ));
      else if(condition == 2) return m/square(s);
      else reject("calc_param: unsupported condition =", condition);
      return negative_infinity();
    }
    else reject("calc_param: there is no parameter number ", code);
    return negative_infinity();
  }
  
  vector calc_theta(vector theta_hat, real param1, real param2, real condition){
    if(condition == 1){
      vector[num_elements(theta_hat)] theta_log = exp(theta_hat);
      return theta_log;
    }
    else if(condition == 2){
      vector[num_elements(theta_hat)] theta_gamma = theta_hat/param2;
      return theta_gamma;
    }
    else {
      reject("model_lpdf: unsupported condition =", condition);
      return rep_vector(negative_infinity(),num_elements(theta_hat));
    }
  }
}

data {
  int<lower=0> N;                                  // number of data points
  int<lower=0> n_subjects;                         // number of subjects
  array[N] int <lower=1, upper=n_subjects> id;      // subject ID
  vector[N] y;                                     // response variable
  
  // model condition
  int<lower=1, upper=2> condition; // 1 = log normal, 2 = gamma
                                   
  // Prior hyperparameters                                                                    
  real mean_theta_prior_mu;
  real <lower = 0> mean_theta_prior_sigma;       // hyperpara for log-normal prior on mean of the distribution
  real sd_theta_prior_mu; 
  real <lower = 0> sd_theta_prior_sigma;         // hyperpara for log-normal prior on sd of the distribution
}

parameters {                                                                                
  real <offset = mean_theta_prior_mu, multiplier = mean_theta_prior_sigma> mean_theta_hat;
  real <offset = sd_theta_prior_mu, multiplier = sd_theta_prior_sigma> sd_theta_hat;
  
  vector <lower = (condition == 2 ? 0 : negative_infinity())> [n_subjects] theta_hat; //CHECK OB SO FUNKT/SYN KORREKT MIT ==2!
  real <lower = 0> sigma_epsilon; 
}

transformed parameters {                                                            
  real <lower = 0> mean_theta = exp(mean_theta_hat);            // prior log normal distributed
  real <lower = 0> sd_theta = exp(sd_theta_hat);                // prior log normal distributed
  
 // model parameter calculation
 real <lower = (condition == 2 ? 0 : negative_infinity())> param1 = calc_param(mean_theta, sd_theta, 1, condition);
 real <lower = 0> param2 = calc_param(mean_theta, sd_theta, 2, condition);
 
 // calculation of theta
 vector <lower=0> [n_subjects] theta = calc_theta(theta_hat, param1, param2, condition);
}

model {
 // Priors
  target += normal_lpdf(sd_theta_hat | sd_theta_prior_mu, sd_theta_prior_sigma);
  target += normal_lpdf(mean_theta_hat | mean_theta_prior_mu, mean_theta_prior_sigma);  

 // theta conditioned on model                                                    
  target += model_lpdf(theta_hat | param1, param2, condition);
 
 // measurement error
  target += -log(sigma_epsilon);                    // Jeffreys prior on sigma2
  
 // Likelihood
  target += normal_lpdf(y | theta[id], sigma_epsilon);
}

generated quantities {
  // rename parameter
  real mu_theta; 
  real sigma_theta;
  real alpha_theta; 
  real beta_theta; 
  
  if(condition == 1){
    mu_theta = param1;
    sigma_theta = param2;
  }
  else if(condition == 2){
    alpha_theta = param1;
    beta_theta = param2;
  }
}
