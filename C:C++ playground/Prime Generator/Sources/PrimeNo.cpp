#include "../Headers/PrimeNo.h"
#include <iostream>

PrimeNo::PrimeNo(): primeList(0){
    //Akho Need.
}

PrimeNo::~PrimeNo(){
    delete [] primeList;
}

PrimeNo::PrimeNo(PrimeNo & bpi){
    *primeList = *(bpi.primeList);
}

const PrimeNo PrimeNo::operator=(const PrimeNo & bpi){
    if(this != &bpi){
        primeList = bpi.primeList;
    }

    return *this;
}
void PrimeNo::generatePrimes(int NoOfPrimes){
    primeList = new int[NoOfPrimes];
    int j = 0;
    int primeFac = NoOfPrimes * 0.2;
    for(int i = 0; i <= NoOfPrimes * primeFac ; i++){
        if(isPrime(i,NoOfPrimes)){
            primeList[j] = i;
            std::cout << i << ", " ;
            j++;
        }
    }

}

bool PrimeNo::isPrime(int PrimeCan, int primeAmt){
    int PrimeAcc = 0;
    if(PrimeCan != 0){
        for(int i = 1; i<=primeAmt*10; i++){
          if(PrimeCan%i == 0){
                PrimeAcc++;
            }
        }
    }
    return (PrimeAcc == 2) ? true:false;
}

void PrimeNo::printPrimes(std::ostream& os, int PrimeArr){

    for(int i = 0; i <= PrimeArr ; i++){
        if(primeList[i] != 0){
            os << primeList[i] << " , " ;
        }
    }
}

int PrimeNo::primeVal(int NoOfPrimes, int primePos){
    generatePrimes(NoOfPrimes);
    return primeList[primePos-1];
}