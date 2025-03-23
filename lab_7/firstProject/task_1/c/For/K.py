a = int(input())
sum = 0
numbers = []

for i in range(1,a+1):
    num = int(input())
    numbers.append(num)

for i in numbers:
    sum+=i
print(sum)

