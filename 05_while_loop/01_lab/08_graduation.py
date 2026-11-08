name = input()

counter = 1
total_sum = 0
excluded = 0
is_graduated = True

while counter <= 12:
    grade = float(input())

    if grade < 4.00:
        excluded += 1
        if excluded >= 2:
            is_graduated = False
            print(f"{name} has been excluded at {counter} grade")
            break
        continue

    total_sum += grade
    counter += 1

if is_graduated:
    average_grade = total_sum / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
