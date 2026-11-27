total_tickets = 0
total_student = 0
total_standard = 0
total_kid = 0

movie = input()

while "Finish" != movie:
    free_seats = int(input())
    sold_tickets = 0
    student = 0
    standard = 0
    kid = 0

    ticket = input()

    while "End" != ticket:
        if ticket == "student":
            student += 1
        elif ticket == "standard":
            standard += 1
        elif ticket == "kid":
            kid += 1

        sold_tickets += 1

        if sold_tickets == free_seats:
            break

        ticket = input()

    hall_percent = sold_tickets / free_seats * 100
    print(f"{movie} - {hall_percent:.2f}% full.")

    total_tickets += sold_tickets
    total_student += student
    total_standard += standard
    total_kid += kid

    movie = input()

student_percent = total_student / total_tickets * 100
standard_percent = total_standard / total_tickets * 100
kid_percent = total_kid / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
