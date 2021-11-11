#include <iostream>
#include <string>
#include <iomanip>
#include <armadillo>
#include <random>
#include "spin_system.hpp"

using namespace std;
using namespace arma;

SpinSystem::SpinSystem(int L, string spinconfig)
{
  L_in = L;
  n_spins_in = L * L;

  if (spinconfig == "ordered")
  {
    spin_mat_in = imat(L, L).fill(1);
  }
  if (spinconfig == "unordered")
  {
    spin_mat_in = randi<imat>(L, L, distr_param(0, 1)) * (2) - 1;
  }
  initialize();
}

//Function for computing the initial energy and magnetization of the spin system

void SpinSystem::initialize()
{
  energy_in = 0;
  magn_in = 0;
  for (int i = 0; i < L_in; i++)
  {
    for (int j = 0; j < L_in; j++)
    {
      energy_in -= spin_mat(i, j) * (spin_mat(i + 1, j) + spin_mat(i, j + 1));
      magn_in += spin_mat(i, j);
    }
  }
}

//Implementing the periodic boundary conditions in our spin matrix

int SpinSystem::spin_mat(int i, int j)
{
  return spin_mat_in(idx(i), idx(j));
}

//Index to impose periodic boundary conditions

int SpinSystem::idx(int index)
{
  return (index + L_in) % L_in;
}

//g++ -std=c++11 -larmadillo spin_system.cpp && ./a.out
//g++ -std=c++11 -c spin_system.cpp
