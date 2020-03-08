#!/usr/bin/python


#Getting user input of how many people are at dinner
while True:
    try:
        num_of_people = int(input("Welcome to my tip calculator, please enter how many people are at the table: \n"))
        break
    except ValueError:
        print("you must enter an integer \n")
        continue
    else:
        break


#Creating objects for people to hold names and totals
class people:
    def __init__(self, name, total):
        self.name = name
        self.total = total

#Create a while loop to create objects for each person

#Create a counter to run with the loop and a List to hold the obj
loopCounter = 0
listPeople = []

#Loop for adding people to the list
while loopCounter != num_of_people:


    #Want to make sure the user's name is stored as a string variable, so we're going to use raw_input
    personName = input("Please enter a person's name  \n")
    personName = str(personName)

    #Making sure the user's total is an float
    personTotal = float(input("Please enter that person's total  \n"))
    #Appending the obj to the list
    listPeople.append(people(personName, personTotal))

    #Loop variable to break when we've hit the total == number of people
    loopCounter += 1

#Calculating the tip and tax portion each person will have to pay
subTotal = float(input("Please enter the subtotal amount  \n"))
tipTotal = float(input("Please enter the total including tip + tax  \n"))
tipandtax = tipTotal/subTotal



#Printing the list to make sure the values are properly populated
for obj in listPeople:
    print(obj.name, round(obj.total * tipandtax, 2), sep = " ")




    



