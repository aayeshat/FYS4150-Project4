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
  SpinSystem system(L, "unordered");
  cout << "main" << endl;
  //SpinSystem system2 = new SpinSystem(L);
  // cout << system.L_in << endl;

  // system.init_spin_mat();
  // arma_rng::set_seed_random();
  // imat spin_mat_rand = randi<imat>(L, L, distr_param(0,1))*(2) - 1;
  //cout << spin_mat_rand << endl;
  system.initialize();

  int no_cycles = 10000;

  Ising run(L, T, "unordered");
  run.montecarlo(T, no_cycles);
  cout << run.exp_vals << endl;


return 0;
}



//g++ -std=c++11 -larmadillo main.cpp && ./a.out
