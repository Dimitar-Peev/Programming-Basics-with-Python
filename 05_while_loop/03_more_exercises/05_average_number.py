n = int(input())

total = 0

for _ in range(n):
    number = int(input())
    total += number

average = total / n

print(f"{average:.2f}")