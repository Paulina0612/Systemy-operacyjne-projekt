#define ITERATIONS 100

#include "table.h"

int N = 0; // Amount of philosophers

Table* table;

void *PhilosopherActivity(void *arg);
void DiningPhilosophersProblem();

int main(int argc, char *argv[]) {
	if(argc>1){
		N=strtol(argv[1], argv, 10);

        table = new Table(N);
        if(table == NULL || table->philosophers == NULL){
            cout << "Allocating memory failed.";
            return -1;
        }
        
        DiningPhilosophersProblem();
    }
    else {
        cout << "No argument given.";
        return -1;
    }
	return 0;
}

void *PhilosopherActivity(void *arg)
{
    int a = 0;
    int i = *(int *)arg;
    while (a<ITERATIONS){
        sleep(1);
        table->TakeFork(i);
        sleep(0.5);
        table->PutFork(i);
        a++;
    }
}

void DiningPhilosophersProblem(){
    pthread_t thread_id[N]; // Declaration of an array of threads for philosophers
    
    pthread_attr_t attr; // Declaration of an attribute of threads
    pthread_attr_init(&attr);

    for (int i = 0; i < N; i++) {
        pthread_create(&thread_id[i], &attr, PhilosopherActivity, &table->philosophers[i].index);
        cout << "Philosopher number " << i << " is thinking" << endl;
    }

    // Destroying
    pthread_attr_destroy(&attr);
    pthread_exit(NULL);
}