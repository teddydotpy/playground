#include <vector>

#ifndef VECTORMATH_H
#define VECTORMATH_H

class VectorMath{

    public:
    VectorMath(std::vector<float> p_Vector);
    VectorMath operator+(const VectorMath &ight);
    VectorMath operator-(const VectorMath &ight);
    std:vector<float> VectorAdd(std::vector<float> left, std::vector<float> right);
    void VectorMinus(std::vector<float> left, std::vector<float> right);
    // I think using floating point numbers for the vecctor operations is good here 
    //because a lot of the work i will be working on will be floating point
    // right ?? 
    // i'll just change to in when neccessary... i hope it's not a lot.


    
    private:
    std::vector<float> nVector;


};

#endif