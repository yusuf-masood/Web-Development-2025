import math
a = int(input())
d = []
for i in range(2,a+1):
    if a%i == 0:
        d.append(i)
print(d[0])

