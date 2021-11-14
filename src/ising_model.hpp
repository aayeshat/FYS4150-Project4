#ifndef ISING_MODEL_HPP
#define ISING_MODEL_HPP

#include <armadillo>
#include <string>
#include "spin_system.hpp"

using namespace arma;
using namespace std;

class Ising
{
private:
  void metropolis(SpinSystem system);

public:
  int L_in;
  int n_spins_in;
  int n_spins_squared_in;
  double beta_in;
  vec w;
  vec exp_vals;
  string spinconfig_in;
  vec exp_e, exp_m;
  ivec mc_cycles;

  Ising(int L, double T, string spinconfig);

  void montecarlo(double T, int no_cycles);
  void output(double T, int no_cycles);
};

#endif
