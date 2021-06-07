#! /usr/bin/env python3

Temperature = input("Please enter the current Temperature as an whole number: ")
#User inputs the temperature.

if int(Temperature) >= 21:
    print("The current temperature is: " + Temperature + " degrees celsius")
    print(" Summer is here. ")
else:
    print("The current temperature is: " + Temperature + " degrees celsius")
    print("Welcome to winter.")

