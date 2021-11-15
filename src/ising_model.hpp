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
  vec boltzmann;
  vec exp_vals;
  string spinconfig;
  vec exp_e;
  vec exp_m;
  ivec mc_cycles;

  Ising(int L, double T, string spinconfig);

  void montecarlo(double T, int no_cycles);
  void output(double T, int no_cycles);
};

#endif
