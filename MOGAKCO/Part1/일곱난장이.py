lst = []
for i in range(9):
    lst.append(int(input()))

def seven(lst):
    s = sum(lst)
    for i in lst:
        for j in lst:
            if i != j:
                a = s - i - j
                if a == 100:
                    lst.remove(i)
                    lst.remove(j)
                    return lst


answer = sorted(seven(lst))

for i in answer:
    print(i)