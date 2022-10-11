a, b = map(int, input().split())
lst = []
cnt = 1
i = 1
while cnt <= b:
    for j in range(i):
        lst.append(i)
        cnt += 1
    i += 1

answer = sum(lst[a-1:b])
print(answer)
    
