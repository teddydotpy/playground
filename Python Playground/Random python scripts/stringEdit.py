#! /usr/bin/env python3

headlineStr = input("Please enter today's newspaper headline: ")

capitalizehead = headlineStr.capitalize()
strlen = len(headlineStr)
strMax = max(headlineStr)
strMin = min(headlineStr)
strTitle = headlineStr.title()

#We print all the relevant information.
print("Headline: " + headlineStr)
print("Capitalized headline: " + capitalizehead)
print("Headline title: " + strTitle)
print("The Min character is: " + strMin)
print("The Max character is: " + strMax)
print("The string has a lenght of: " + str(strlen))

