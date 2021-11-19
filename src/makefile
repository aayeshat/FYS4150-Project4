
all: compile run

compile:
	c++ main_8.cpp spin_system.cpp ising_model.cpp -o main.o -std=c++11 -larmadillo

run: ./main.o

clean: rm -f *.o *~

#use as: make all


all_parallel: compile_par

compile_par:
	c++ main_8.cpp spin_system.cpp ising_model.cpp -o main.o -std=c++11 -larmadillo -lomp -Xpreprocessor -fopenmp

run_par: ./main.o

clean_par: rm -f *.o *~
