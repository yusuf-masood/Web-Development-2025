# N = int(input())
# numbers = []

# for i in range(N):
#     num = int(input())
#     numbers.append(num)
    
# for i in numbers:
#     if i%2==0:
#         print(i,end=" ")


N = int(input())

numbers = list(map(int, input().split()))

for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
