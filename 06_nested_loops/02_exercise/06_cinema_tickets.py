movie_name = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while "Finish" != movie_name:
    free_seats = int(input())

    seats_taken = 0

    while seats_taken < free_seats:
        ticket_type = input()

        if ticket_type == "End":
            break

        seats_taken += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

    percent_full = seats_taken / free_seats * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    movie_name = input()

total_tickets = student_tickets + standard_tickets + kid_tickets
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100:.2f}% kids tickets.")
