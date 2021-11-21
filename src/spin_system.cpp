#include "spin_system.hpp"

SpinSystem::SpinSystem(int L_in, std::string spinconfig_in)
{
  L = L_in;
  n_spins = L * L;

  if (spinconfig_in == "ordered")
  {
    spin_mat = imat(L, L).fill(1);
  }
  if (spinconfig_in == "unordered")
  {
    spin_mat = 2 * randi<imat>(L, L, distr_param(0, 1)) - 1;
  }
  initialize();
}

//Function for computing the initial energy and magnetization of the spin system

void SpinSystem::initialize()
{
  energy = 0;
  magn = 0;
  for (int i = 0; i < L; i++)
  {
    for (int j = 0; j < L; j++)
    {

      energy -= spin_mat(i, j) *
                (spin_mat(idx(i, -1), j) + spin_mat(i, idx(j, 1)));

      magn += spin_mat(i, j);
    }
  }
}

//Implementing the periodic boundary conditions in our spin matrix

int SpinSystem::spin_matrix(int i, int j)
{
  return spin_mat(idx(i, 0), idx(j, 0));
}

int SpinSystem::idx(int index, int add)
{
  return (index + L + add) % L;
}

//g++ -std=c++11 -larmadillo spin_system.cpp && ./a.out
//g++ -std=c++11 -c spin_system.cpp
