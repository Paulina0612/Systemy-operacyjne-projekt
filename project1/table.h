#include "philosopher.h"

class Table
{
    public: 
        Philosopher *philosophers;
        pthread_mutex_t mutexLock;
        int N;

        Table(int N)
        {
            this->N = N;
            philosophers = (Philosopher*)malloc(N * sizeof(Philosopher));

            for (int i = 0; i < N; i++)
            {
                philosophers[i].index = i;
                philosophers[i].state = THINKING;
            }

            for (int i = 0; i < N; i++)
            {
                pthread_cond_init(&philosophers[i].conditionVariable, NULL);
            }

            pthread_mutex_init(&mutexLock, NULL);
        }

        // Check if Philosopher can eat 
        void CheckConditionsForPhilosopher(int n)
        {
            if (philosophers[(n+1)%N].state != EATING && philosophers[(n-1)%N].state!= EATING 
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


        // Put Fork function
        void PutFork(int n)
        {
            pthread_mutex_lock(&mutexLock); // Lock mutex
            philosophers[n].state = THINKING; // Indicates that the philosopher is thinking

            CheckConditionsForPhilosopher((n+1)%N);
            CheckConditionsForPhilosopher((n-1)%N);

            pthread_mutex_unlock(&mutexLock); // Unlock mutex
        }
};