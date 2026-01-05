a = input()
b = [int(i) for i in input().split()]
c = b[0]
e = 0

for i in b:
    if i > c:
        c = i
    elif i < c:
        e += (c-i)
print(e)
