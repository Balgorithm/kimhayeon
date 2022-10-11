t = int(input())

for i in range(t):
    s = []
    n = int(input())
    while n != 0:
        s.append(n % 2)
        n //= 2

    for j in range(len(s)):
        if s[j] == 1:
            print(j , end=" ")