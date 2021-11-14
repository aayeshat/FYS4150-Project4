#ifndef SPINSYSTEM
#define SPINSYSTEM

#include <string>
#include <iostream>
#include <string>
#include <iomanip>
#include <armadillo>
#include <random>

using namespace arma;
using namespace std;

class SpinSystem
{
private:
  void initialize();
  int idx(int index);

public:
  int L_in, n_spins_in;
  double energy_in, magn_in;
  imat spin_mat_in;

  SpinSystem(int L, std::string spinconfig);
  int spin_mat(int i, int j);
};

#endif
