#ifndef ISING_MODEL_HPP
#define ISING_MODEL_HPP

#include <armadillo>

using namespace arma;
using namespace std;

class Ising{
public:

  Ising(int L, double T, string spinconfig);

  int L_in, n_spins_in;
  double beta_in;
  vec w, exp_vals;
  string spinconfig_in;

  //void metropolis(SpinSystem *system);
  void metropolis();
  void montecarlo(double T, int no_cycles);

};

#endif
