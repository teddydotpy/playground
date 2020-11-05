#ifndef ROOTFINDERS_H
#define ROOTFINDERS_H
#include <iostream>

class Rootfinders{
    public:
    Rootfinders();
    ~Rootfinders();
    void getFunction();
    // Make sure to remind the user that the 
    // ^ square sign will be instead replaced with ** .
    
    bool tol(); 
    //The tolerance, ie the value that the approximation
    //has to get under.
    

};

#endif