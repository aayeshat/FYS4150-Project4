
all: compile run

compile:
	g++ ./src/main.cpp ./src/spin_system.cpp ./src/ising_model.cpp -o main.o -std=c++11 -larmadillo 

run: ./main.o

clean: rm -f *.o *~

#use as: make
