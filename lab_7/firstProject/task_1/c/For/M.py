a = int(input())
sum_zero = 0
numbers = []

for i in range(1,a+1):
    num = int(input())
    if num ==0:
        numbers.append(num)
print(len(numbers))


