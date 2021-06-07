#! /usr/bin/env python3

''' Private” instance variables that cannot be accessed except from 
inside an object don’t exist in Python '''

class Dog:
    def __init__(self):
        self.dogName = ""
        self.dogBreed = ""
        self.dogStatus = ""
        self.dogDOB = 0
    
    def populate(self, dogName, dogBreed, dogStatus, dogDOB):
        self.dogName = dogName
        self.dogBreed = dogBreed
        self.dogStatus = dogStatus
        self.dogDOB = dogDOB

    def display(self):
        print("Dog Name: " + self.dogName + '\n'
                "Dog Breed: " + self.dogBreed + '\n'
                "Dog Status: " + self.dogStatus + '\n'
                "Dog Date of Birth: " + self.dogDOB )
    
    def userInput(self):
        name = input("Please enter your dogs name: ")
        Breed = input("Please enter the breed: ")
        Status = input("Please enter the dog's status: ")
        DoB = input("Please enter the Date of Birth(dd mmmm yyyy): ")

        self.populate(name, Breed, Status, DoB)

newDog = Dog()
newDog.userInput()
newDog.display()






