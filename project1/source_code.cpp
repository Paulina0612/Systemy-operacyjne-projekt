#include "table.h"

int N = 0; // Amount of philosophers

Table* table;

void *PhilosopherActivity(void *arg);

void DiningPhilosophersProblem();

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
    
    DiningPhilosophersProblem();

	return 0;
}

void *PhilosopherActivity(void *arg)
{
    int i = 0;
    while (true)
    {
        int i = *(int *)arg;
        sleep(1);
        table->TakeFork(i);
        sleep(0.5);
        table->PutFork(i);
        i++;
    }
}

void DiningPhilosophersProblem(){
    pthread_t thread_id[N]; // Declaration of an array of threads for philosophers
    pthread_attr_t attr; // Declaration of an attribute of threads
}