
all: compile run

compile:
	c++ main_8.cpp spin_system.cpp ising_model.cpp -o main.o -std=c++11 -larmadillo

run: ./main.o

clean: rm -f *.o *~

#use as: make all

all_parallel: compile_par

compile_par:
	c++ main_8.cpp spin_system.cpp ising_model.cpp -o main_8.o -std=c++11 -larmadillo -lomp -Xpreprocessor -fopenmp

run_par: ./main_8.o

clean_par: rm -f *.o *~

all_main0: compile_0

compile_0:
	c++ main.cpp spin_system.cpp ising_model.cpp -o main0.o -std=c++11 -larmadillo

run_0: ./main0.o

clean_0: rm -f *.o *~
