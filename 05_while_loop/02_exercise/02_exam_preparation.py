number_poor_grades = int(input())

solved_problems_count = 0
failed_times = 0
sum_grades = 0
last_problem = ""

input_line = input()
while "Enough" != input_line:
    current_grade = int(input())

    if current_grade <= 4:
        failed_times += 1

    if failed_times == number_poor_grades:
        print(f"You need a break, {failed_times} poor grades.")
        break

    sum_grades += current_grade
    solved_problems_count += 1
    last_problem = input_line

    input_line = input()

else:
    average_grade = sum_grades / solved_problems_count
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {solved_problems_count}")
    print(f"Last problem: {last_problem}")
