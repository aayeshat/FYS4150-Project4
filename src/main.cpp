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
  double Z_hyp = 4. * (cosh(8.) + 3);

  double E_big = -32. / Z * sinh(8.); //riktig for E
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
  string temp = "1.0"; //T=1.0J/kB and T=2.4J/kB,
  double T = stod(temp);

  //  analytic(T);

  int no_cycles = 1000000; //no. of monte carlo cycles

  string spinconfig = "ordered"; //"ordered" eller "unordered"

  Ising ising(L, T, spinconfig);
  ising.montecarlo(T, no_cycles);
  ising.mc_cycles.save("../out/data/montecarlo_cycles.txt", raw_ascii);
  ising.exp_e.save("../out/data/energy_T" + temp + "_" + spinconfig + "_problem5.txt", raw_ascii);
  ising.exp_m.save("../out/data/magnetization_T" + temp + "_" + spinconfig + "_problem5.txt", raw_ascii);
  ising.exp_C_v.save("../out/data/heatcapacity" + temp + "_" + spinconfig + "_problem5.txt", raw_ascii);
  ising.exp_X.save("../out/data/susceptivility" + temp + "_" + spinconfig + "_problem5.txt", raw_ascii);
  
  
  
  return 0;

}

//g++ -std=c++11 -larmadillo main.cpp && ./a.out
