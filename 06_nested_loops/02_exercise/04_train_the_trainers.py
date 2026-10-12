jury_count = int(input())

input_line = input()

total_sum_grades = 0
presentation_count = 0

while "Finish" != input_line:
    presentation_name = input_line

    sum_current_grades = 0
    for _ in range(jury_count):
        current_grade = float(input())
        sum_current_grades += current_grade

    average = sum_current_grades / jury_count
    total_sum_grades += average
    presentation_count += 1

    print(f"{presentation_name} - {average:.2f}.")

    input_line = input()

final_assessment = total_sum_grades / presentation_count
print(f"Student's final assessment is {final_assessment:.2f}.")
