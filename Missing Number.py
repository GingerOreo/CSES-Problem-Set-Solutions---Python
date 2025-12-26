n = int(input())
missing = n * (n + 1) // 2 - sum(map(int, input().split()))
print(missing)
