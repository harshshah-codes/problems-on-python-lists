# Program to remove duplicates from a list.
from utils import createList

# Creating the list
L = createList(25, 100)

# Removing duplicates
out = list(set(L)) 

print("Orignal List:", L)
print("Output list:", out)