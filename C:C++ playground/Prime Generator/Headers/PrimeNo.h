#ifndef PRIMENO_H
#define PRIMENO_H
#include <iostream>

class PrimeNo{
    public:
        PrimeNo();
        ~PrimeNo();
        PrimeNo(PrimeNo & bpi) ;
        //bpi == BEFORE PRIME INSTANCE 
        const PrimeNo operator=(const PrimeNo & bpi);
        bool isPrime(int PrimeCan, int PrimeAmt);
        void generatePrimes(int NoOfPrimes);
        void printPrimes(std::ostream& os, int primeArrSize);
        int primeVal(int NoOfPrimes,int prPos);

    private:
        int * primeList;
};

#endif