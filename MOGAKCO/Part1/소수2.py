a = int(input())
b = int(input())
answer = 0
m = b
def sosu(n):
    if n < 2 : return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for i in range(a,b+1):
    if sosu(i):
        answer += i
        if m > i :
            m = i


if answer == 0:
    print(-1)
else:
    print(answer)
    print(m)
