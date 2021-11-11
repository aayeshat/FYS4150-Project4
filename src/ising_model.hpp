#ifndef ISING_MODEL_HPP
#define ISING_MODEL_HPP

#include <armadillo>

using namespace arma;
using namespace std;

class Ising
{
public:
  int L_in;
  int n_spins_in;
  int n_spins_squared_in;
  double beta_in;
  vec w;
  vec exp_vals;
  string spinconfig_in;
  vec exp_e, exp_m;

  Ising(int L, double T, string spinconfig);

  //void metropolis(SpinSystem *system);
  void metropolis();
  void montecarlo(double T, int no_cycles);
  void output(double T, int no_cycles);
};

#endif
