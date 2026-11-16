first_number = input()
second_number = input()

f1, f2, f3, f4 = int(first_number[0]), int(first_number[1]), int(first_number[2]), int(first_number[3])
s1, s2, s3, s4 = int(second_number[0]), int(second_number[1]), int(second_number[2]), int(second_number[3])

for first_digit in range(f1, s1 + 1):
    for second_digit in range(f2, s2 + 1):
        for third_digit in range(f3, s3 + 1):
            for fourth_digit in range(f4, s4 + 1):
                # if first_digit % 2 != 0 and second_digit % 2 != 0 and third_digit % 2 != 0 and fourth_digit % 2 != 0:
                if all(x % 2 != 0 for x in [first_digit, second_digit, third_digit, fourth_digit]):
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')
