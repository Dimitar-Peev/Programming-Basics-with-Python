a = int(input())
b = int(input())
max_passwords = int(input())

count = 0
A = 35
B = 64

for x in range(1, a + 1):
    for y in range(1, b + 1):
        if count == max_passwords:
            break

        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")

        A += 1
        B += 1

        if A > 55:
            A = 35
        if B > 96:
            B = 64

        count += 1

    if count == max_passwords:
        break