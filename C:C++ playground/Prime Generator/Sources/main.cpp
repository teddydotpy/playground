#include <iostream>
#include <chrono>
#include <fstream>
#include "../Headers/PrimeNo.h"

int main(){
    PrimeNo tryObj;
    std::ofstream utfile;
    utfile.open("fool.txt");
    if(utfile.fail()){
        std::exit(1);
    }
    int sizedof, pos;

    std::cout << "Enter prime size and pos: " ;
    std::cin >> sizedof >> pos;

    auto start1 = std::chrono::high_resolution_clock::now();
    tryObj.generatePrimes(sizedof);
    auto stop1 = std::chrono::high_resolution_clock::now();

    auto start2 = std::chrono::high_resolution_clock::now();
    tryObj.printPrimes(utfile, sizedof);
    auto stop2 = std::chrono::high_resolution_clock::now();

    auto start3 = std::chrono::high_resolution_clock::now();
    utfile << std::endl << "The prime in Position " << pos << " is: " << tryObj.primeVal(sizedof,pos) << std::endl;
    auto stop3 = std::chrono::high_resolution_clock::now();

    auto duration1 = std::chrono::duration_cast<std::chrono::minutes>(stop1 - start1);
    auto duration2 = std::chrono::duration_cast<std::chrono::minutes>(stop2 - start2);
    auto duration3 = std::chrono::duration_cast<std::chrono::minutes>(stop3 - start3);
    
    std::cout << "The generatePrimes function takes: " << duration1.count() << " seconds" << std::endl ;
    std::cout << "The PrintPrimes function takes: " << duration2.count() << " seconds" << std::endl ;
    std::cout << "The PrimeVal function takes: " << duration3.count() << " seconds" << std::endl ;
        
    return 0;
}