# Dining Philosophers Problem

## Launching instruction 
1. To launch this program download code to your computer and unzip it. 
2. Launch terminal in folder Systemy-operacyjne-projekt.
3. Run command
   ````md
   g++ ./project1/source_code.cpp -o ./project1/source_code
   ````
5. Run command
   ````md
   ./project1/source_code.exe {N}
   ````
   where {N} is the number of philosophers.

## Description
The Dining Philosophers Problem is a synchronization problem in computer science. It involves a group of N philosophers sitting around a circular table, each alternating between thinking and eating. To eat, a philosopher needs two chopsticks or forks, one on their left and one on their right. However, each chopstick is shared between two adjacent philosophers.

The challenge is to design a strategy that allows all philosophers to eat without causing deadlock (where no one can proceed) or starvation (where some philosophers never get a chance to eat). The problem illustrates issues in concurrent programming, such as resource allocation and synchronization.

## Code explanaition

### Threads
Each philosopher in the code is represented as a thread. Philosophers function is presented below.

````c++
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
````

### Critical sections
Critical sections are parts of code, where threads have access to shared resources (in this case forks). In the code there are three critical sections.

1. Taking fork
   ````c++
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
   ````
2. Putting fork
   ````c++
   // Put Fork function
   void PutFork(int n)
   {
       pthread_mutex_lock(&mutexLock); // Lock mutex
       philosophers[n].state = THINKING; // Indicates that the philosopher is thinking

       CheckConditionsForPhilosopher((n+1)%N);
       CheckConditionsForPhilosopher((n-1)%N);

       pthread_mutex_unlock(&mutexLock); // Unlock mutex
   }
   ````
3. Checking if philosopher can start eating
   ````c++
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
   ````

