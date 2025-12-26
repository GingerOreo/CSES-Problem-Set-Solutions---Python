import math

a = int(input())
b = a*(a+1)/2
d = a
if b % 2 != 0 or b == 1:
    print("NO")
else:
    print("YES")
    print(math.floor(a/2))
    print(d, end=" ")
    while d - 3 > 0:
        d -= 3
        print(d, end=" ")
        if d - 1 > 0:
            d -= 1
            print(d, end=" ")
    d = a-1
    print()
    print(math.ceil(a/2))
    print(d, end=" ")
    d -= 1
    print(d, end=" ")
    while d - 3 > 0:
        d -= 3
        print(d, end=" ")
        if d - 1 > 0:
            d -= 1
            print(d, end=" ")