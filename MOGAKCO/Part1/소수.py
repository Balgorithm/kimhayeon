def sosu(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



t = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    if sosu(i):
        cnt += 1

print(cnt)
        


