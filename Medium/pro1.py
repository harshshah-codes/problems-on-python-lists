# Program to find the second-largest element in a list.
from utils import createList 

L = createList(25, 100)


for i in L:
    min = L[0]
    for j in L:
        if min > j:
            min = j
    out.append(min)
    L.remove(min)