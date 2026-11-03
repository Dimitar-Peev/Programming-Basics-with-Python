n = int(input())

first_sum = 0
previous_sum = 0
max_diff = 0
all_equal = True

for _ in range(n):
    a = int(input())
    b = int(input())

    pair_sum = a + b

    if first_sum == 0:
        first_sum = pair_sum
    else:
        diff = abs(pair_sum - previous_sum)
        if diff > max_diff:
            max_diff = diff

        if pair_sum != first_sum:
            all_equal = False

    previous_sum = pair_sum

if all_equal:
    print(f"Yes, value={first_sum}")
else:
    print(f"No, maxdiff={max_diff}")
