#include "philosopher.h"

int N = 0; // Amount of philosophers


Philosopher *philosophers;

int main(int argc, char *argv[]) {
	if(argc>1){
		N=strtol(argv[1], argv, 10);
	}
    else {
        cout << "No argument given.";
        return -1;
    }

    philosophers = (Philosopher*)malloc(N * sizeof(Philosopher));

    if(philosophers==NULL){
        cout << "Allocating memory for philosophers failed.";
        return -1;
    }


	return 0;
}