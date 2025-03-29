#define THINKING 0
#define EATING 1
#define WAITING 2

#include <iostream>
#include <stdlib.h>  // for strtol
#include <unistd.h>
using namespace std;


// Philosopher semaphore 
struct Philosopher
{
    public:
        int state;
        pthread_cond_t conditionVariable; 
};

