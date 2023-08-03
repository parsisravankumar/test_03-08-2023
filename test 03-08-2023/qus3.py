"""3. Merge the following lists
given 
l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]
output = [1, 3, 4, 7, 8, 9, 10]"""
l1 = [1, 4, 7, 9]
l2 = [3, 8, 10]

l = set(l1 + l2)
result = list(l)

print(result) 