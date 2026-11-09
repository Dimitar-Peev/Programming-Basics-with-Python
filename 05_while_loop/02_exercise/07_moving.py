width = int(input())
length = int(input())
height = int(input())

volume = width * length * height

sum_boxes = 0
not_enough_space = False

input_line = input()
while "Done" != input_line:
    current_boxes = int(input_line)
    sum_boxes += current_boxes

    if sum_boxes >= volume:
        not_enough_space = True
        break

    input_line = input()

diff = abs(sum_boxes - volume)
if not_enough_space:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")
