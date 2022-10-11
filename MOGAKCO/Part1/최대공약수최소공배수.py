a, b = map(int, input().split())

if a < b:
    a, b = b, a
def lcm(a, b):
    c = gcd(a, b)
    k = a // c
    l = b // c
    return c * k * l
    

def gcd(a, b):
    if b == 0:
        return a

    else:
        return gcd(b, a%b)


print(gcd(a, b))
print(lcm(a, b))