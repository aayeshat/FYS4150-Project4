# Project4

The topic of this project is the Ising model in two dimensions. We will use this simple model to explore temperature-dependent behaviour in ferromagnets. A particular goal is to numerically estimate the critical temperature at which our 2D system undergoes a phase transition, from a magnetized phase to a phase with no net magnetization.
On the methodological side, our focus in this project is the Markov Chain Monte Carlo method for sampling from probability distributions of many variables, and how the resulting samples can be used to approximate probability distributions and expectation values for derived quantities; and using parallelization to speed up our code.

The  code is implemented for the Ising model and uses the Markov Chain Monte Carlo approach to sample spin configurations (Metropolis algorithm).
The  src contains the all the source files cpp and hpp. The spin_system contains initial spin configuration either ordered or random (unordered) initially.
All the physical quantities mentioned below energy, magnetization to be considered per spin. Python contains python scripts for all plots while in out there is data and generated plots for Project 4


g++ ./src/main.cpp ./src/spin_system.cpp ./src/ising_model.cpp -larmadillo

g++ main.cpp spin_system.cpp ising_model.cpp -larmadillo

g++ main_8.cpp spin_system.cpp ising_model.cpp -larmadillo

