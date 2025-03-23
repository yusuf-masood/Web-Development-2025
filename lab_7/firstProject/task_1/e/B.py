
def power(a,b):
    if b>=0:
        return pow(a,b)
    else:
        return 1/pow(a, abs(b))

a,b = map(int,input().split())
result = power(a,b)
print(result)
