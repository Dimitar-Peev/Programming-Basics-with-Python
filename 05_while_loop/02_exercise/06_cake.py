width = int(input())
length = int(input())

total_count_pieces = width * length

input_line = input()
while "STOP" != input_line:
    current_pieces = int(input_line)

    total_count_pieces -= current_pieces

    if total_count_pieces <= 0:
        print(f"No more cake left! You need {abs(total_count_pieces)} pieces more.")
        break

    input_line = input()

else:
    print(f"{total_count_pieces} pieces are left.")
