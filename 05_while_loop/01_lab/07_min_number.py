input_line = input()

if "Stop" == input_line:
    print("No numbers were entered")
else:
    min_num = int(input_line)

    input_line = input()

    while "Stop" != input_line:
        current_num = int(input_line)

        if current_num < min_num:
            min_num = current_num

        input_line = input()

    print(min_num)