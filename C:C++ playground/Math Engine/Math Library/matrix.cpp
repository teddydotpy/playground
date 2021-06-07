#include <iostream>
#include <string>

#include "headers/matrix.h"

template<class t>
M_Matrix<t>::M_Matrix(){
    matrix = new t((new t(2), new t(2)));
}

template<class t>
M_Matrix<t>::M_Matrix(const M_Matrix & cp_Mat){
    this->matrix = new int [nrows][CONSTANT];
}

template<class t>
M_Matrix<t>::~M_Matrix(){

}