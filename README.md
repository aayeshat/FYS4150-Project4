# Project4


--- Repo is a little messy now ---
Check branch cana for what we did with parallelization, latest python script etc --

makefile for mac only:

main_8.cpp contains the parallelized code and writes to file

build: make all_par 

run: ./main_8.o

main.cpp contains what we did initially, like comparing numerical and exact values

build: make all_main0

run: ./main0.o

------

The topic of this project is the Ising model in two dimensions. We will use this simple model to explore temperature-dependent behaviour in ferromagnets. A particular goal is to numerically estimate the critical temperature at which our 2D system undergoes a phase transition, from a magnetized phase to a phase with no net magnetization.
On the methodological side, our focus in this project is the Markov Chain Monte Carlo method for sampling from probability distributions of many variables, and how the resulting samples can be used to approximate probability distributions and expectation values for derived quantities; and using parallelization to speed up our code.

The  code is implemented for the Ising model and uses the Markov Chain Monte Carlo approach to sample spin configurations (Metropolis algorithm).
The  src contains the all the source files cpp and hpp. The spin_system contains initial spin configuration either ordered or random (unordered) initially. Also, in ising metropolis and monte carlo is implmented and all the required parameters are calculated.
All the physical quantities mentioned below energy, magnetization to be considered per spin. Python contains python scripts for all plots while in out there is data and generated plots for Project 4

The  main.cpp is designed to compute analytically and numerically energy , magnetization and specific heat and susceptibility for a lattice size L=2 and 20 for temperature 1 J/kB. Saves in text files. For L=2, T=1 J/kB compares the numerical values with the analytical.
In main_8.cpp the burn-in time is defined after reaching this all theparameters are calculated against temperature range{2.1,2.4}, initial condition is chosen to be random. 


g++ ./src/main.cpp ./src/spin_system.cpp ./src/ising_model.cpp -larmadillo

g++ main.cpp spin_system.cpp ising_model.cpp -larmadillo

g++ main_8.cpp spin_system.cpp ising_model.cpp -larmadillo

