N = int(input())
postive_num = []

array = list(map(int, input().split()))
for i in array:
    if i>0:
        postive_num.append(i)
print(len(postive_num))






# # Read the input
# N = int(input())
# array = list(map(int, input().split()))

# # Count the number of positive numbers in the array
# count_positive = sum(1 for num in array if num > 0)

# # Print the count of positive numbers
# print(count_positive)




# a = int(input())
# numbers = []

# for i in range(0, a):
#     num = int(input())
#     if num < 0:
#         numbers.append(num)

# print(len(numbers))
