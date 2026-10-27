n = int(input())

first_number = int(input())
max_number = first_number
min_number = first_number

for _ in range(n - 1):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
