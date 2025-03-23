def find_min(a, b, c, d):
    return min(a, min(b, min(c, d)))


a, b, c, d = map(int, input().split())
result = find_min(a, b, c, d)
print(result)
