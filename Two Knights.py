n = int(input())
for i in range(1,n+1):
    a = (i**2)*((i**2)-1)/2
    b = (i-2)*(i-1)*4
    print(int(a - b))

    