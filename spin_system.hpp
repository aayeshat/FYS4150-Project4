#ifndef SPINSYSTEM
#define SPINSYSTEM

#include <armadillo>

using namespace arma;
using namespace std;

class SpinSystem{
public:

  SpinSystem(int L, string spinconfig);

  int L_in, n_spins_in;
  double energy_in, magn_in;
  imat spin_mat_in;

  //arma_rng;
  random_device rd;
  mt19937 gen;
  uniform_real_distribution<double> random_number;

  int idx(int index);
  void initialize();
  int spin_mat(int i, int j);

};

#endif
