import math
a = int(input())
d = []
for i in range(1,a+1):
    if a%i == 0:
        d.append(i)
print(len(d))

