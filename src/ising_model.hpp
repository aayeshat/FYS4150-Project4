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
  void metropolis(SpinSystem& system);
  void initBoltzmann();

public:
  int L;
  int n_spins;
  double beta;
  int burnin_t;
  vec boltzmann;
  vec exp_vals;
  string spinconfig;
  vec exp_e;
  vec exp_m;
  vec  exp_C_v;
  vec  exp_X;
  vec energy_samples;
  ivec mc_cycles;

  Ising(int L, double T, int burnin_t, string spinconfig);

  void montecarlo(double T, int no_cycles);
};

#endif
