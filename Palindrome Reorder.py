input = list(input())
list_palindrome = []
even_list = []
odd_list = []
b = 0

for i in set(input):
    x = input.count(i)
    if x % 2 == 1:
        b += 1
    if b > 1:
        print('NO SOLUTION')
        break
    for a in range(0,x):
        if x % 2 == 0:
            even_list.append(i)
        else:
            b += 1
            odd_list.append(i)

if b < 2:
    for i in even_list:
        list_palindrome.insert(len(list_palindrome)//2,i)
    for i in odd_list:
        list_palindrome.insert(len(list_palindrome)//2,i)
    listy = ' '.join(list_palindrome).replace(" ","")
    print(listy)