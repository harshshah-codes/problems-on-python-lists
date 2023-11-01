# Program to find the largest element in a list.
from utils import createList

# Creating the list
L = createList(25, 100)

# Finding the max elem element 
max_elem = max(L)

print("Orignal List:", L)
print("Maximum Element:", max_elem)