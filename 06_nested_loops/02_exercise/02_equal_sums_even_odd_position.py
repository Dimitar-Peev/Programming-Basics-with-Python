start = int(input())
end = int(input())

for number in range(start, end + 1):
    current_num_str = str(number)

    even_sum = 0
    odd_sum = 0

    for index, digit in enumerate(current_num_str):

        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if even_sum == odd_sum:
        print(current_num_str, end=" ")
