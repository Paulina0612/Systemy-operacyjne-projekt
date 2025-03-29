#include "philosopher.h"

class Table
{
    public: 
        Philosopher *philosophers;


        Table(int N)
        {
            philosophers = (Philosopher*)malloc(N * sizeof(Philosopher));

            
        }
};