#! /usr/bin/env python3

fileEdit = open("MyCovidNotes.txt" , "a")
print("Ten COVID Facts")

for i in range(10):
    Covidfact = input("Input covid fact number " + str(i + 1) + ": ")
    fileEdit.write(Covidfact + '\n')

fileEdit.close()
fileEdit = open("MyCovidNotes.txt" , "r")
print(fileEdit.read())
fileEdit.close()
