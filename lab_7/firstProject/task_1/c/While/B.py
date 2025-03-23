# import math

# numbers = []
# N = int(input())

# a = 2
# while a <= N:
#     if 15%a==0:
#         numbers.append(a)
#     a += 1
# print(numbers)
# print(numbers[0])

import math

N = int(input())

smallest_divisor = None
a = 2
while a <= math.sqrt(N):
    if N % a == 0:
        smallest_divisor = a
        break
    a += 1

if smallest_divisor is None:
    smallest_divisor = N

print(smallest_divisor)
