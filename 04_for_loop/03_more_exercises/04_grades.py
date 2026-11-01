students = int(input())

top = 0
between_4_and_5 = 0
between_3_and_4 = 0
fail = 0
total_grade = 0

for _ in range(students):
    grade = float(input())
    total_grade += grade

    if grade >= 5.00:
        top += 1
    elif grade >= 4.00:
        between_4_and_5 += 1
    elif grade >= 3.00:
        between_3_and_4 += 1
    else:
        fail += 1

top_percent = top / students * 100
between_4_and_5_percent = between_4_and_5 / students * 100
between_3_and_4_percent = between_3_and_4 / students * 100
fail_percent = fail / students * 100
average = total_grade / students

print(f"Top students: {top_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_5_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_4_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average:.2f}")
