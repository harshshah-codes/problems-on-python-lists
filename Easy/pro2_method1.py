# Program to find the largest element in a list.
from utils import createList

# Creating the list
L = createList(25, 100)

# Finding the max elem element 
max_elem = L[0]

for x in L:
    if x > max_elem:
        max_elem = x

print("Orignal List:", L)
print("Maximum Element:", max_elem)