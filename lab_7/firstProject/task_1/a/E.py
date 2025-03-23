def find_stopping_point(v, t):
    total_distance = 109  # Length of the Moscow Ring Road
    stopping_point = (v * t) % total_distance
    return stopping_point

# Input
v = int(input())
t = int(input())

# Calculate stopping point
result = find_stopping_point(v, t)
print( result)
