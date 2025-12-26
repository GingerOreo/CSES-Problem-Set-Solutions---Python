n = int(input())
c = 0
for i in range(0,n):
    y, x = [int(i) for i in input().split()]
    if y > x:
        if y % 2 == 0:
            c = y*(y-1)+1
            c += 1*(y-x)
        else:
            c = y*(y-1)+1
            c -= 1*(y-x)
    elif y < x:
        if x % 2 == 0:
            c = x*(x-1)+1
            c -= 1*(x-y)
        else:
            c = x*(x-1)+1
            c += 1*(x-y)
    else:
        c = x*(y-1)+1
    print(c)
