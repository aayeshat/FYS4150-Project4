#include <iostream>
#include <iomanip>
#include <armadillo>
#include <random>
#include "ising_model.hpp"

Ising::Ising(int L_in, double T_in, string spinconfig_in)
{
  L = L_in;
  n_spins = L * L;
  spinconfig = spinconfig_in;
  beta = 1. / T_in; //k = J = 1
  exp_vals = vec(4);

  initBoltzmann();
}

void Ising::initBoltzmann()
{

  boltzmann = vec(17, fill::zeros);

  //Compute array w containing possible Delta_E values from -8J to 8J
  for (int i = -8; i <= 8; i += 4)
  {
    boltzmann(i + 8) = exp(-1. *  beta * i);
  }
}

void Ising::metropolis(SpinSystem& system)
{

  //Mersienne Twister random number generator
  random_device rd;
  mt19937_64 gen(rd());
  uniform_real_distribution<double> random_number(0.0, 1.0);
  uniform_real_distribution<double> random_to_L(0.0, L);

  for (int n = 0; n <= n_spins; n++)
  {

    //Choose a random spin in lattice
    int i = random_to_L(gen);
    int j = random_to_L(gen);

    //Calculate energy difference from all neighbouring spins

    int delta_E = 2 * system.spin_matrix(i, j)      //
                  * (system.spin_matrix(i, j + 1)   //
                     + system.spin_matrix(i, j - 1) //
                     + system.spin_matrix(i + 1, j) //
                     + system.spin_matrix(i - 1, j));

    //
    //Metropolis test
    //
    //if dE < 0; accept
    //if dE > 0; compute w = exp(-beta*dE) and perform test:
    //compare boltzmann with random number r, if r < boltzmann; accept

    if (delta_E <= 0)
    {
       system.spin_mat(i, j) *= -1; //flip spin

      system.energy += delta_E;
      
      //accept and add energy
      system.magn += 2 * system.spin_mat(i, j); //update magnetization of new spin configuration

    }
    //if dE > 0, (pre-calculated in boltzmann), flip spin and compare boltzmann with random number, and if < boltzmann; accept
    else if (random_number(gen) < boltzmann(delta_E + 8))
    {
      system.spin_mat(i, j) *= -1;

      system.energy += delta_E;
      system.magn += 2 * system.spin_mat(i, j);
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
  //double exp_e = 0;
  //double exp_m = 0;
  exp_e = vec(no_cycles, fill::zeros);
  exp_m = vec(no_cycles, fill::zeros);
  mc_cycles = ivec(no_cycles, fill::zeros);

  arma_rng::set_seed_random();


  SpinSystem system(L, spinconfig);
  for (int cycle = 1; cycle <= no_cycles; cycle++)
  {

    metropolis(system);
  
    exp_E += system.energy;
    exp_E_sq += system.energy * system.energy;
    exp_M += abs(system.magn);
    exp_M_sq += system.magn * system.magn;

    double norm = 1. / (double)(cycle * n_spins);

    //Samples
    mc_cycles(cycle - 1) = cycle;
    exp_e(cycle - 1) = exp_E * norm;
    exp_m(cycle - 1) = exp_M * norm;
  }

  //Final values
  //Compute energy and magnetization per spin
  exp_E /= n_spins * no_cycles;
  exp_E_sq /= n_spins * n_spins * no_cycles;
  exp_M /= n_spins * no_cycles;
  exp_M_sq /= n_spins * n_spins * no_cycles;

  exp_vals(0) = exp_E;
  exp_vals(1) = exp_E_sq;
  exp_vals(2) = exp_M;
  exp_vals(3) = exp_M_sq;
}

void Ising::output(double T, int no_cycles)
{

  // SpinSystem system(L, spinconfig);
  // metropolis();
  // Ising ising(L, T, "ordered");
  // ising.montecarlo(T, no_cycles);
  //
  // ofstream fout;
  // fout.open("./out/data/montecarlo_cycle_expE_expM.txt");
  // // exp_e = exp_E * norm;
  // // exp_m = exp_M * norm;
  // fout << ising.exp_e << ising.exp_m << endl;
  // fout.close();
}
