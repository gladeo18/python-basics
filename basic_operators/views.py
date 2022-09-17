import operator

from operator import index
from pickle import TRUE
from django.shortcuts import render

def arithmetic(choice, num1, num2):

    ops= {"a": operator.add, "b": operator.sub, "c": operator.mul, "d": operator.truediv, "e": operator.mod, "f": operator.pow}
    print("ANSWER IS: ", ops[choice](num1, num2), "\n")


def inputs(choice):    # Error handling for non-integer operands.

    try:
        num1 = float(input ("Enter first number: "))
        num2 = float(input ("Enter second number: "))
        arithmetic(choice, num1, num2)
    except ValueError:
        print("\nThe value you entered is not a number.", end = " ")
        inputs(choice)
    
choice = " "

while choice != "g":
    
    within_range = False

    print("Please select the operator of your choosing:")
    print("[a] Addition  [b] Subtraction  [c] Multiplication [d] Division [e] Modulus [f] Exponent [g] Exit")
    choice = input("Choice: ").lower()

    for i in range(ord('a'), ord('g')):
        if choice == chr(i):
            inputs(choice)
            within_range = True  
            
    if choice != "g" and not within_range:  # If "choice" is not within a-g range.
        print("\nInvalid input.", end = " ")

print("Exit\n")  # If "choice" is g

