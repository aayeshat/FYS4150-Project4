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
  int idx(int index, int add);

public:
  int L;
  int n_spins;
  double energy;
  double magn;
  imat spin_mat;

  SpinSystem(int L, std::string spinconfig);
  int spin_matrix(int i, int j);
};

#endif
