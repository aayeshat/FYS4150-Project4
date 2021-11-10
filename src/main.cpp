#include <iostream>
#include <string>
#include <iomanip>
#include <armadillo>
#include <random>
#include "spin_system.hpp"
#include "ising_model.hpp"

using namespace std;
using namespace arma;

void analytic(double T)
{
  double Z = 4. * (cosh(2) + 3);               //Marias
  double Z_2 = 2. * exp(-2) + 2 * exp(2) + 12; //min, blir feil
  double e_exc = -8. / Z_2 * sinh(2);
  double e_exc_sq = 16. / Z * (2);

  double Z_big = 4. * (4. * cosh(8.) + 3); //riktig for E
  double E_big = -32. / Z_big * sinh(8.);  //riktig for E

  double e_exc_E = -8 / Z_big * sinh(8);

  double m_exc = 1. / Z * (2 * exp(2.) + 1);
  double m_exc_sq = 1. / (2 * Z) * (4 * exp(1) + 1);

  double m_ = (1. / Z_big) * (2 * exp(8) + 4);

  cout << "big E " << E_big << endl; //riktig for E
  cout << "e_exc " << e_exc << endl; //resultat halvparten av E
  cout << "e_exc_sq  " << e_exc_sq << endl;
  cout << "big E2? " << e_exc_E << endl;
  // cout << "m  " << m_exc << endl;
  // cout << "m squared " << m_exc_sq << endl;
  cout << "m " << m_ << endl;
}

int main()
{

  int L = 2;
  double T = 1.;

  int no_cycles = 1000; //no. of monte carlo cycles

  Ising ising(L, T, "ordered");
  ising.montecarlo(T, no_cycles);
  cout << "exp_vals" << endl
       << ising.exp_vals << endl;

  analytic(T);

  return 0;
}

//g++ -std=c++11 -larmadillo main.cpp && ./a.out
