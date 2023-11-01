import random

def createList(n, range_L):
    """
        Accepts:
            n(Integer): length of list to be created
            range_L(Integer): A range from which values will be picked in the list

        Returns:
            L: A list of integers
    """

    L = []

    for i in range(n):
        elem = random.random() * range_L
        L.append(elem)

    return L