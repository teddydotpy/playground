#! /usr/bin/env python3

#Since Python does not have a switch implimentation i will be blasphemeos and use an annoying 
# amount of if else statements... sorry.
def monthConv(nMonthnum):
    if nMonthnum == 1:
        return "January"
    elif nMonthnum == 2:
        return "February"
    elif nMonthnum == 3:
        return "March"
    elif nMonthnum == 4:
        return "April"
    elif nMonthnum == 5:
        return "May"
    elif nMonthnum == 6:
        return "June"
    elif nMonthnum == 7:
        return "July"
    elif nMonthnum == 8:
        return "August"
    elif nMonthnum == 9:
        return "September"
    elif nMonthnum == 10:
        return "October"
    elif nMonthnum == 11:
        return "November"
    elif nMonthnum == 12:
        return "December"
    else:
        return "That is not a month."

def myDate(nDay, nMonth, nYear):
    youName = input("Enter your name: ")
    return "On " + str(nDay) + " " + monthConv(int(nMonth)) + " " + str(nYear) + " " + youName + " was born."


inpDay = input("Please enter a birthday Day(dd): ")
inpMonth = input("Please enter a birthday Month(mm): ")
inpYear = input("Please enter a birthday Year(yyyy): ")

theMessage = myDate(inpDay, inpMonth, inpYear)
print(theMessage)