ones = int(input())
twos = int(input())
fives = int(input())
target = int(input())

for count_1 in range(ones + 1):
    for count_2 in range(twos + 1):
        for count_5 in range(fives + 1):
            total = count_1 * 1 + count_2 * 2 + count_5 * 5

            if total == target:
                print(f"{count_1} * 1 lv. + {count_2} * 2 lv. + {count_5} * 5 lv. = {target} lv.")