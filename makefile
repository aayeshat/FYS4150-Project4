
all: compile run

compile:
	g++ -std=c++11 -larmadillo main.cpp spin_system.cpp ising_model.cpp -o main.out

run: ./main.out

#clean: rm -f *.o *~

#use as: make
