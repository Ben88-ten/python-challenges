
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

todo = input('what would you like to do today - add, subtract, divide, multiply')

#Options
responseOne = input('Enter first number')
responseTwo = input('Enter second number')

# Converts to numbers
num1 = int(responseOne)
num2 = int(responseTwo)



# Calc

def calculate(num1, num2):
    if todo == ("add"):
        print("result" ,num1 + num2)
    elif todo == "subtract":
        print("result" , num1 - num2)
    elif todo == "multiply":
        print("result" ,num1 - num2)
    elif todo == "divide":
        print("result" ,num1 / num2)
    else:
        print('Enter a number')

(calculate(num1,num2))
