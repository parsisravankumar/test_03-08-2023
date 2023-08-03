"""2. 
10
10 9
10 9 8
10 9 8 7
10 9 8 7 6"""

n = 10
for i in range(n, 5, -1):
        for j in range(n, i - 1, -1):
            print(j, end=' ')
        print()