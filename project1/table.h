#include "philosopher.h"

class Table
{
    public: 
        Philosopher *philosophers;
        pthread_mutex_t mutexLock;


        Table(int N)
        {
            philosophers = (Philosopher*)malloc(N * sizeof(Philosopher));\
        }

        // Check if Philosopher can eat 
        void CheckConditionsForPhilosopher(int n)
        {
            if (philosophers[(n+1)%5].state != EATING && philosophers[(n-1)%5].state!= EATING 
                && philosophers[n].state == WAITING)
                {
                    philosophers[n].state = EATING;

                    pthread_cond_signal(&philosophers[n].conditionVariable);
                }
        }


        // Take Fork function
        void TakeFork(int n)
        {
            pthread_mutex_lock(&mutexLock); // Lock mutex
            philosophers[n].state = WAITING; // Indicates that the philosopher is waiting 
            CheckConditionsForPhilosopher(n); // Test if philosopher can eat 

            // If philosopher is unable to eat wait for the signal
            if (philosophers[n].state != EATING)
                pthread_cond_wait(&philosophers[n].conditionVariable, &mutexLock);
            cout << "Philosopher number " << n << " is eating" << endl;

            pthread_mutex_unlock(&mutexLock); // Unlock mutex
        }
};