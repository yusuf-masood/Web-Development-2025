N = int(input())
large_num = []
count = 0

array = list(map(int, input().split()))
for i in range(1,N):
    if array[i]>array[i-1]:
        count +=1
print(count)