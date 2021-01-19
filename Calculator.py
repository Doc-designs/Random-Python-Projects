import math
import turtle

def exponent(equation):
    halves = equation.split("^", 1)
    return int(halves[0])**int(halves[1])
def multiplication():
    return null
def devision():
    return null
def addition():
    return null
def subtraction():
    return null
def parentheses():
    return null
def equivilance():
    return null

#Combines the functions together for larger equation handling
def calculator():
    equation = input("Enter an Equation: ")
    currentDigit = ""
    digitList = []
    calculating = True
    while calculating == True:
        for i in range(len(equation)):
            if equation[i].isdigit() == True:
                currentDigit = currentDigit + equation[i]
            elif equation[i].isdigit() == False and currentDigit != "":
                digitList.append(currentDigit)
                currentDigit = ""
            if i+1 == len(equation):
                digitList.append(currentDigit)
                currentDigit = ""
        return print(equation.find(digitList[0])+len(digitList[0])-1)
        
    
        #if equation[i] == "(":
            #if equation[i-1].isdigit() == True:

            if equation[i] == "^":
                fullNumberOne = 1
                fullNumberTwo = 1
            if equation[i-1].isdigit() == True:
                while equation[i-fullNumberOne].isdigit() == True:
                    fullNumberOne += 1
                while equation[i+fullNumberTwo].isdigit() == True:
                    fullNumberTwo += 1
                exponent(equation[i-fullNumberOne:i+fullNumberTwo])
    
        #if equation[i] == "*":

        #if equation[i] == "/":

        #if equation[i] == "+":

        #if equation[i] == "-":
