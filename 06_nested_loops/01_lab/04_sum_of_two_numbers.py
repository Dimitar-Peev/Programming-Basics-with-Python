start = int(input())
end = int(input())
magic_number = int(input())

count = 0
is_found = False

for first in range(start, end + 1):
    for second in range(start, end + 1):
        count += 1

        if first + second == magic_number:
            print(f"Combination N:{count} ({first} + {second} = {magic_number})")
            is_found = True
            break

    if is_found:
        break

if not is_found:
    print(f"{count} combinations - neither equals {magic_number}")