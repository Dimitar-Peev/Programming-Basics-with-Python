m = int(input())

count_valid_4 = 0
pass_a = 0
pass_b = 0
pass_c = 0
pass_d = 0

for a in range(1, 10):
    for b in range(1, 10):
        if a >= b:
            continue

        for c in range(1, 10):
            for d in range(1, 10):
                if c <= d:
                    continue

                control = a * b + c * d
                if control == m:
                    count_valid_4 += 1

                    print(f"{a}{b}{c}{d}", end=" ")

                    if count_valid_4 == 4:
                        pass_a = a
                        pass_b = b
                        pass_c = c
                        pass_d = d

print()
if count_valid_4 >= 4:
    print(f"Password: {pass_a}{pass_b}{pass_c}{pass_d}")
else:
    print("No!")
