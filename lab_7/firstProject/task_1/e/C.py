def xor(x, y):
    return int((x and not y) or (not x and y))

if __name__ == "__main__":
    x, y = map(int, input().split())
    result = xor(x, y)
    print(result)
