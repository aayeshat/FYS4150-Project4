
all: compile run

compile:
	c++ main.cpp spin_system.cpp ising_model_parallel.cpp -o main.o -std=c++11 -larmadillo -lomp -Xpreprocessor -fopenmp

run: ./main.o

clean: rm -f *.o *~

#use as: make all
