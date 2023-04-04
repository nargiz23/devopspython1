
number = 12345

# extract each digit of the number
digit1 = number // 10000
number %= 10000
digit2 = number // 1000
number %= 1000
digit3 = number // 100
number %= 100
digit4 = number // 10
number %= 10
digit5 = number


reversed_number = digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1

print(reversed_number)
