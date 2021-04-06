#print("Welcome to Chase bank.")
#print("Have a nice day!")

import time

print("Welcome to Chase bank.")

time.sleep(3)

Name = input("What is your name?")

liste = ["Smith", "1960" , 3000]



if  Name == liste[0]:
    print ("dear Mr. " + Name)
    age = input("Please enter your date of birth to confirm:")

if age == liste[1]:

    todo = input("Thank you, what would you like to do? Withdraw (1) Deposit (2) Balance (3) Exit (4)")
else:
     print("You are not registered! Goodbye")



def take_off_1():

     if todo == "1":
            take_off = int(input("how much would you like to withdraw? "))
            print("Thank you, your new balance is up" + ": ")
            print (liste[2] - take_off)

def deposit_2():
     if todo == "2":
             deposit = int(input("how much would you like to deposit?"))
             print("Thank you, your new balance is up" + ": ")
             print (liste[2] + deposit)

def Account_balance_3():
     if todo == "3":
             print ("Your current account balance is" + ": " + liste[2] + "EUR" )
             input("What do you want to do? Withdraw (1) Deposit (2) Balance (3) Exit (4)")

def Quit_4():
     if todo == "4":
           print("Have a nice day!")




take_off_1()
deposit_2()
Account_balance_3()
Quit_4()
