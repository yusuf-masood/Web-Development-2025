
# N = int(input())

# numbers = []
# for i in range(0, N):
#     num = int(input())
#     numbers.append(num)

# for i in range(0, len(numbers), 2):
#     print(numbers[i], end=" ")



N = int(input())


numbers = list(map(int, input().split()))


for i in range(0, len(numbers), 2):
    print(numbers[i], end=" ")
