cnt = 0
l = 0
for i in range(10):
    a, b = map(int, input().split())
    cnt -= a
    cnt += b
    if l < cnt:
        l = cnt

print(l)
