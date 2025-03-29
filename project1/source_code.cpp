#include <iostream>
#include <stdlib.h>  // for strtol

using namespace std;

int N = 0; // Amount of philosophers


int main(int argc, char *argv[]) {
	if(argc>1){
		N=strtol(argv[1], argv, 10);
	}

	return 0;
}