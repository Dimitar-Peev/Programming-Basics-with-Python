upper1 = int(input())
upper2 = int(input())
upper3 = int(input())

for first in range(1, upper1 + 1):
    for second in range(1, upper2 + 1):
        for third in range(1, upper3 + 1):
            if first % 2 == 0 and third % 2 == 0 and second in (2, 3, 5, 7):
                print(f"{first} {second} {third}")