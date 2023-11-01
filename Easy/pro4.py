# Program to check if a list is empty.
from utils import createList

# Creating the lists
L_filled = createList(25, 100)
L_empty = createList(0, 0)

if L_filled:
    print(f"{L_filled} is not empty")
else:
    print(f"{L_filled} is empty")
# This will give output: Not empty

if L_empty:
    print(f"{L_empty} is not empty")
else:
    print(f"{L_empty} is empty")
# This will give output: '[] is empty'