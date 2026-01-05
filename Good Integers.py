a = 0
n = input()
x = n[0]
for i in n:
    if i == x:
        a += 1
        if a == 3:
            print("Yes")
            break
    else:
        a = 0
        x = i
if a != 3:
    print("No")
        