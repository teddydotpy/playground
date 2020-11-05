#! /usr/bin/env python3
stdentNO = ""
stdsum = 0

for i in range(8):
    iterstdno = input("Please enter your student number one number at a time " + str(i) + ": ")
    stdentNO += iterstdno
    stdsum += int(iterstdno) 

print("The student number is: " + str(stdentNO))
print("Sum of all the numbers: " + str(stdsum))
print("Average of all the numbers: " + str(stdsum/8))
for i in range(8):
    print(stdentNO[i])
