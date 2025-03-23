import math

N = int(input())

a = 1
while a <= N:
    if int(math.sqrt(a)) ** 2 == a:
        print(a, end=" ")
    a += 1
