#ifndef M_MATRIX
#define M_MATRIX

#include <iostream>
#include <string>

template<class T>
class M_Matrix{

    public:
    M_Matrix();
    M_Matrix(const M_Matrix & cp_Mat);
    M_Matrix(int size); //Returns a square size x size matrix
    M_Matrix(int row, int col); // not square matrix
    ~M_Matrix();
    
    M_Matrix m_Mult(M_Matrix matB);
    M_Matrix m_Add(M_Matrix MatB);
    M_Matrix m_Subtract(M_Matrix MatB);
    String stringify();

    private:
    T* matrix;

};

#endif