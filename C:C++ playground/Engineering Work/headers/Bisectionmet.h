#ifndef BISECTIONMET_H
#define BISECTIONMET_H

#include "Rootfinders.h"
#include <iostream>

class Bisectionmet: public Rootfinders{
    public: 
    Bisectionmet();
    ~Bisectionmet();
    void calcapprox();
    void printApprox();


    private:
    float firstEndpt, lastEndpt, midpt;
    float calcMidpt(float endpt1, float endpt2);
    bool tol(float approx);
   
    
};

#endif