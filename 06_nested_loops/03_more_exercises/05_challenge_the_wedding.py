men = int(input())
women = int(input())
tables = int(input())

count = 0

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        if count == tables:
            break
        print(f"({man} <-> {woman})", end=" ")
        count += 1
    if count == tables:
        break