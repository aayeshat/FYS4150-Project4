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
  double Z = 2. * exp(-8) + 2 * exp(8) + 12;
  double Z_hyp = 4. * ( cosh(8.) + 3);


  double E_big = -32. / Z * sinh(8.);  //riktig for E
  double E_sq = 2. / Z * (256 * cosh(8));
  double M_big = 8. / Z * (exp(8) + 2);
  double M_sq = 32. / Z * (exp(8) + 1);

  double e = -8. / Z * sinh(8.);
  double e_sq = 16. / Z * cosh(8);
  double m = 2. / Z * (2 + exp(8));
  double m_sq = 2. / Z * (1 + exp(8));

  cout << "big E " << E_big << endl;
  cout << "big E squared " << E_sq << endl;
  cout << "big M " << M_big << endl;
  cout << "big M squared " << M_sq << endl;

  cout << "e " << e << endl;
  cout << "e squared " << e_sq << endl;
  cout << "m " << m << endl;
  cout << "m squared " << m_sq << endl;
}

int main()
{

  int L = 2;
  double T = 1.;

  int no_cycles = 10000; //no. of monte carlo cycles

  Ising ising(L, T, "ordered");
  ising.montecarlo(T, no_cycles);
  cout << "exp_vals" << endl
       << ising.exp_vals << endl;

  analytic(T);

  return 0;
}

//g++ -std=c++11 -larmadillo main.cpp && ./a.out
