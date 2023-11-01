# Program to count the occurrences of an element in a list.
from utils import createList

# Creating list
L = createList(25, 100)

# Finding frequency of each element
freq = { }

for x in L:
  if not x in freq:
    freq[x] = 0
  freq[x] += 1

print("Original List:", L)
print("Frequency: ", freq)