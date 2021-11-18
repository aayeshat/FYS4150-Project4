#include <iostream>
#include <string>
#include <iomanip>
#include <armadillo>
#include <random>
#include "spin_system.hpp"
#include "ising_model.hpp"

using namespace std;
using namespace arma;

int main()
{
  int burnin_t = 10;

  string spinconfig = "unordered"; //"ordered" or "unordered"
  int no_cycles = 100;

  double min_t = 2.1;
  double max_t = 2.4;
  double step_size = 0.003;
  int n_step = (max_t - min_t) / step_size + 1;

  int L_array[4] = {20, 40, 80, 100};

  for (int L_index = 0; L_index < 4; L_index++)
  {
    int L = L_array[L_index];

    mat L_exp_vals(n_step + 1, 5);

    for (int ti = 0; ti <= n_step; ti += 1)
    {
      double T = (ti * step_size) + min_t;
      Ising ising(L, T, burnin_t, spinconfig);
      ising.montecarlo(T, no_cycles);

      vec exp_vals = ising.exp_vals;

      L_exp_vals.row(ti).col(0) = T;
      L_exp_vals.row(ti).col(1) = exp_vals(0);
      L_exp_vals.row(ti).col(2) = exp_vals(2);
      L_exp_vals.row(ti).col(3) = exp_vals(4);
      L_exp_vals.row(ti).col(4) = exp_vals(5);
    }

    L_exp_vals.print("T  exp_E   exp_M   C_v    X");
    L_exp_vals.save("../out/data_8/energy_L" + to_string(L) + "_" + spinconfig + "_problem8.txt", raw_ascii);
  }

  return 0;
}

//g++ -std=c++11 -larmadillo main.cpp && ./a.out
