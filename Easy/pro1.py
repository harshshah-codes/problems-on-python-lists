# Program to find the sum of a list of numbers.
from utils import createList

# Creating the list
L = createList(25, 100)

# Finding the sum
sum = 0
for x in L:
    sum += x

# Printing output
print("Orignal list:", L)
print("Sum of list:", sum)