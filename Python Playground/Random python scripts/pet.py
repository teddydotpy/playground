#! /usr/bin/env python3

#function to take in the pet name and type to process data
def myPet(petType, petName):
    print("Your pet is a " + petType)
    print(petName + " is a cute pet name.")

inpetName = input("Input pet name: ")
inppettpy = input("Input pet type: ")

myPet(inppettpy, inpetName)