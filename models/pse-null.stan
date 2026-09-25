
data {
  int <lower = 0> N;
  int <lower = 0> n_subjects;
  array[N] int id;
  vector[N] y;
}


parameters {    // model parameters that are inferred in model (which priors exist for)
  real <lower = 0> sigma_epsilon;
}


model {
  // Priors
  target += -log(sigma_epsilon);  // Jeffreys prior on sigma2
  
  // Likelihood
  target += normal_lpdf(y | 0, sigma_epsilon);
}
