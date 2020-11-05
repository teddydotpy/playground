#!/usr/bin/env python3

fib_val_arr = [1,1]


def fib_Generator(fib_val_pos):
    #The part that generates the values for the array
    for i in range(2, fib_val_pos):
        fib_val_arr.insert(i,fib_val_arr[i-2] + fib_val_arr[i-1]) 
    print(fib_val_arr)
    print (fib_val_pos)
    return fib_val_arr[fib_val_pos - 1]

if __name__ == "__main__":
    print ("Enter fibonacci val you want: ")
    input_val = int(input())
    print(fib_Generator(input_val))
