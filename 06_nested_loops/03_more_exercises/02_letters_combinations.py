start = input()
end = input()
skip = input()

count = 0

for first in range(ord(start), ord(end) + 1):
    for second in range(ord(start), ord(end) + 1):
        for third in range(ord(start), ord(end) + 1):
            first_char = chr(first)
            second_char = chr(second)
            third_char = chr(third)

            if first_char != skip and second_char != skip and third_char != skip:
                print(f"{first_char}{second_char}{third_char}", end=" ")
                count += 1

print(count)