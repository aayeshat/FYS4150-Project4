#include <iostream>
#include <string>
#include <iomanip>
#include <armadillo>
#include <random>
#include "spin_system.hpp"
#include "ising_model.hpp"

Ising::Ising(int L, double T, string spinconfig)
{
  L_in = L;
  n_spins_in = L * L;
  spinconfig_in = spinconfig;
  n_spins_squared_in = n_spins_in * n_spins_in;
  beta_in = 1. / T; //k = J = 1
  exp_vals = vec(4);
  w = vec(17, fill::zeros);

  metropolis();
}

void Ising::metropolis()
{
  SpinSystem system(L_in, spinconfig_in);

  //Mersienne Twister random number generator
  random_device rd;
  mt19937_64 gen(rd());
  uniform_real_distribution<double> random_number(0.0, 1.0);
  uniform_real_distribution<double> random_to_L(0.0, L_in);

  //Compute array w containing possible Delta_E values from -8J to 8J
  for (int i = 0; i <= 17; i += 4)
  {
    w(i) = exp(-beta_in * (i - 8));
  }

  for (int n = 0; n <= n_spins_in; n++)
  {

    //Choose a random spin in lattice
    int i = random_to_L(gen);
    int j = random_to_L(gen);

    //Calculate energy difference from all neighbouring spins
    int delta_E = 2 * system.spin_mat(i, j) * (system.spin_mat(i, j + 1) + system.spin_mat(i, j - 1) + system.spin_mat(i + 1, j) + system.spin_mat(i - 1, j));

    //
    //Metropolis test
    //

    //if dE < 0; accept
    //if dE > 0; compute w = exp(-beta*dE) and perform test:
    //compare w with random number r, if r < w; accept

    if (delta_E <= 0)
    {
      system.energy_in += delta_E;                    //accept and add energy
      system.spin_mat_in(i, j) *= (-1);               //flip spin
      system.magn_in += 2 * system.spin_mat_in(i, j); //update magnetization of new spin configuration
    }
    //if dE > 0, (pre-calculated in w), flip spin and compare w with random number, and if < w; accept
    else if (random_number(gen) < w(delta_E + 8))
    {
      system.energy_in += delta_E;
      system.spin_mat_in(i, j) *= (-1);
      system.magn_in += 2 * system.spin_mat_in(i, j);
    }
  }
}

void Ising::montecarlo(double T, int no_cycles)
{

  //Initialize expectation values and exp. values squared
  double exp_E = 0;
  double exp_E_sq = 0;
  double exp_M = 0;
  double exp_M_sq = 0;

  ofstream fout;
  fout.open("./out/data/montecarlo_cycle_expE_expM.txt");

  for (int cycle = 0; cycle < no_cycles; cycle++)
  {

    SpinSystem system(L_in, spinconfig_in);
    metropolis();

    exp_E += system.energy_in;
    exp_E_sq += system.energy_in * system.energy_in;
    exp_M += abs(system.magn_in);
    exp_M_sq += system.magn_in * system.magn_in;

    fout << cycle << "   " << exp_E << "   " << exp_E_sq << "   " << exp_M << "   " << exp_M_sq << endl;
  }

  fout.close();

  //Compute energy and magnetization per spin
  exp_E /= n_spins_in * no_cycles;
  exp_E_sq /= n_spins_in * n_spins_in * no_cycles;
  exp_M /= n_spins_in * no_cycles;
  exp_M_sq /= n_spins_in * n_spins_in * no_cycles;

  exp_vals(0) = exp_E;
  exp_vals(1) = exp_E_sq;
  exp_vals(2) = exp_M;
  exp_vals(3) = exp_M_sq;
}
