#include <iostream>
#include <string>
#include <iomanip>
#include <armadillo>
#include <random>
#include "spin_system.hpp"
#include "ising_model.hpp"

using namespace std;
using namespace arma;


int main(){
  int i, j;
  int L = 10;
  double T = 1.;
  SpinSystem system(L, "ordered");
  cout << "main" << endl;
  //SpinSystem system2 = new SpinSystem(L);
  // cout << system.L_in << endl;

  // system.init_spin_mat();
  // arma_rng::set_seed_random();
  // imat spin_mat_rand = randi<imat>(L, L, distr_param(0,1))*(2) - 1;
  //cout << spin_mat_rand << endl;
  system.initialize();

  int no_cycles = 10000;

  Ising run(L, T, "ordered");
  run.montecarlo(T, no_cycles);
  cout << run.exp_vals << endl;

  //analytic
  double Z = 4. * (cosh(2*beta) + 3); //Marias
  double Z_2 = 2. * exp(- 2) + 2 * exp(2) + 12; //mine
  double e_exc = - 8. / Z_2 * (sinh(2 * beta));
  double e_exc_sq = 16. / Z * (2 * beta);

  double e_exc_E = - 8 / Z_2 * (sinh(8 * beta));

  double m_exc = 1. / Z * (2 * exp(2. * beta) + 1);
  double m_exc_sq = 1. / (2 * Z) * (4 * exp(1) + 1);

  double Z_big = 4. * (4. * cosh(8.) + 3); //riktig
  double E_big = -32. / Z_big * sinh(8.); //riktig

  double m_ = (1. / Z_big) * ( 2 * exp(8) + 4);

  cout << "big E  " << E_big << endl;
  cout << "e  " << e_exc << endl;
  // cout << "e_exc_sq  " << e_exc_sq << endl;
  // cout << "big E2" << e_exc_E << endl;
  // cout << "m  " << m_exc << endl;
  // cout << "m squared " << m_exc_sq << endl;
  cout << "m " << m_ << endl;


return 0;
}



//g++ -std=c++11 -larmadillo main.cpp && ./a.out
