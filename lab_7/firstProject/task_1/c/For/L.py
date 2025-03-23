
binary_number = input()

decimal_number = 0
power = len(binary_number) - 1

for digit in binary_number:
    decimal_number += int(digit) * (2 ** power)
    power -= 1

print( decimal_number)

