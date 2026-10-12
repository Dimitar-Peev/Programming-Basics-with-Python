n = int(input())

for number in range(1111, 10000):
    digits = str(number)
    is_special = True

    for digit_char in digits:
        digit = int(digit_char)

        if digit == 0:
            is_special = False
            break

        if n % digit != 0:
            is_special = False
            break

    if is_special:
        print(number, end=" ")