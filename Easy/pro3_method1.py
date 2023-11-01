# Program to remove duplicates from a list.
from utils import createList

# Creating the list
L = createList(25, 100)

# Removing duplicates
out = []

for x in L:
    if not x in out:
        out.append(x)

print("Orignal List:", L)
print("Output list:", out)