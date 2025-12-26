n = int(input())
b = []
c = n-1
if 1 < n < 4:
    print("NO SOLUTION")
elif n == 1:
    print(1)
else:
    while c - 2 > 0:
        print(c, end=" ")
        c -= 2
    print(c, end=" ")
    c = n
    while c - 2 > 0:
        print(c, end=" ")
        c -= 2
    print(c, end=" ")
    
