#! /usr/bin/env python3

main = [ 
    [0.05, 0.07, 0.06, 0.05, 0.23],
    [0.07, 0.10, 0.08, 0.07, 0.32],
    [0.06, 0.08, 0.10, 0.09, 0.33],
    [0.05, 0.07, 0.09, 0.10, 0.31],
]

A_mat = [ 
    [0.05, 0.07, 0.06, 0.05],
    [0.07, 0.10, 0.08, 0.07],
    [0.06, 0.08, 0.10, 0.09],
    [0.05, 0.07, 0.09, 0.10],
]

B_vec = [0.23, 0.32, 0.33, 0.31]

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def pseudoIterative( w, M, A, b, x):
    buff_mat = []
    iters = []
    x_vec = []
    x_buff = x.copy()

    for k in range(20):
        print(x_buff)
        for i in range(len(b)):
            b[i] = b[i] * w

        for i in range(len(A)): 
            buff_mat.append(list([M[i][j] - (w * A[i][j]) for j in range(len(A[i]))]))

        for i in range(len(buff_mat)):
            value = 0
            for j in range(len(buff_mat)):
                value += buff_mat[i][j] * x_buff[j]
            x_vec.append(value)
            x_vec[i] += b[i]

            
        buff_mat.clear()
        x_buff.clear()

        for i in range(len(x_vec)):
            buff_mat.append(truncate(x_vec[i] / M[i][i], 3))

        iters.clear()
        iters.extend(buff_mat)
        x_buff.clear()
        x_buff.extend(iters)
        buff_mat.clear()
        x_vec.clear()


    return iters

def realJacobi(A, b, x):
    matrix_buff = []
    sum_hold = 0
    T_mat = []
    c_vec = []
    x_vec = x.copy()

    for q in range(10):
        print(x_vec)
        matrix_buff.clear()
        c_vec.clear()

        for i in range(len(A)):
            for j in range(len(A[i])):
                if i == j:
                    matrix_buff.append(0)
                else:
                    matrix_buff.append(truncate(A[i][j] / A[i][i], 3))
                    
            T_mat.append(list(i for i in matrix_buff))
            c_vec.append(truncate(b[i] / A[i][i], 3))
            matrix_buff.clear()

        for i in range(len(x_vec)):
            for j in range(len(A[i])):
                sum_hold += truncate(T_mat[i][j] * x_vec[j], 3)

            matrix_buff.append(sum_hold)

        x_vec.clear()
        for i in range(len(matrix_buff)):
            x_vec.append( matrix_buff[i] + c_vec[i])

    return x_vec

def GaussSeidel(A, b, x):
    pass

print(1.1)
print('1.1.1')
pseudoIterative(1, [
    [0.05, 0, 0, 0],
    [0, 0.10, 0, 0],
    [0, 0, 0.10, 0],
    [0, 0, 0, 0.10],
], A_mat, B_vec, [1 , 1, 1, 1])

print('1.1.2')
realJacobi(A_mat, B_vec, [1, 1, 1, 1])

print(2.2)
print('2.2.1')
pseudoIterative(1, [
    [0.05,              0, 0, 0],
    [0.07, 0.10,           0, 0],
    [0.06, 0.08, 0.10,        0],
    [0.05, 0.08, 0.09,     0.10],
], A_mat, B_vec, [1 , 1, 1, 1])

print('2.2.2')



