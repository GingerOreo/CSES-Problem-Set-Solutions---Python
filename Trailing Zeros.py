n = int(input())
x = 5
b = 0
for i in range(1,20):
    x = 5**i
    if n // x < 1:
        break
    else:
        b += n//x
print(int(b))