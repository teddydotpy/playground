#! /usr/bin/env python3

nMasks = 2000
nStudents = 500
nStudGets = nMasks / nStudents
maskRem = nMasks%nStudents

print("There are " + str(nStudents) + " students and " + str(nMasks) + " masks.")
print("Each student gets " + str(nStudGets) + " masks and " + str(maskRem) + " remain.")
