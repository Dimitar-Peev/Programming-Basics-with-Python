n = int(input())

if n == 0:
    print("No")
    print("Diff = 0")
else:
    first_number = int(input())
    max_number = first_number
    total_sum = first_number

    for _ in range(n - 1):
        current_num = int(input())

        if current_num > max_number:
            max_number = current_num

        total_sum += current_num

    other_nums_sum = total_sum - max_number

    if other_nums_sum == max_number:
        print("Yes")
        print(f"Sum = {other_nums_sum}")
    else:
        print("No")
        diff = abs(other_nums_sum - max_number)
        print(f"Diff = {diff}")
