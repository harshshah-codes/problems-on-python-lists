# Program to find the second-largest element in a list.
from utils import createList

L = createList(25, 100)
out = []

# By first principles, i.e. without using the sort() or sorted() method

while L:
    max = L[0]
    for j in L:
        if max < j:
            max = j
    out.append(max)
    L.remove(max)
    
print("Second max element", out[1])