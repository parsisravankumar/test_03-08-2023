"""1. Print all Pairs which make sum N for the given list.
e,g: l = [4, 3, 6, 8, 2, 9, 7,  5]
N = 10,
It should print (4, 6), (8, 2), (3, 7)"""
l = [4, 3, 6, 8, 2, 9, 7,  5]
n = 10
for i, x in enumerate(l):
    for j, y in enumerate(l):
        if i != j and x+y == n:
            print((x, y))
