# Program to merge two lists into a single list.
from utils import createList

L1 = createList(25, 100)
L2 = createList(25, 100)

merged_list_temp = L1 + L2
merged_list = []

while merged_list_temp:
    minim = merged_list_temp[0]

    for x in merged_list_temp:
        if x < minim:
            minim = x

    merged_list.append(minim)
    merged_list_temp.remove(minim)

print("Orignal Lists:", L1, L2, sep="\n")
print("Merged List:", merged_list, sep="\n")