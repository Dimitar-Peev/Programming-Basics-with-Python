input_line = input()

if "Stop" == input_line:
    print("No numbers were entered")
else:
    max_num = int(input_line)

    input_line = input()

    while "Stop" != input_line:
        current_num = int(input_line)

        if current_num > max_num:
            max_num = current_num

        input_line = input()

    print(max_num)