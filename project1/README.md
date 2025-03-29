# Dining Philosophers Problem

## Launching instruction 
1. To launch this program download code to your computer and unzip it. 
2. Launch terminal in folder Systemy-operacyjne-projekt.
3. Run command "g++ ./project1/source_code.cpp -o ./project1/source_code"
4. Run command "./project1/source_code.exe N", where N is the number of philosophers.

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
