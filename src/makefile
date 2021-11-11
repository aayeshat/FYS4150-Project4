
all: compile run

compile:
	g++ main.cpp spin_system.cpp ising_model.cpp -o main.o -std=c++11 -larmadillo

run: ./main.o

clean: rm -f *.o *~

#use as: make
