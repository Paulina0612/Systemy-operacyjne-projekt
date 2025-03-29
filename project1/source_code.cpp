#include "table.h"

int N = 0; // Amount of philosophers

Table* table;

int main(int argc, char *argv[]) {
	if(argc>1){
		N=strtol(argv[1], argv, 10);
	}
    else {
        cout << "No argument given.";
        return -1;
    }

    table = new Table(N);

    if(table == NULL || table->philosophers == NULL){
        cout << "Allocating memory failed.";
        return -1;
    }
    
	return 0;
}