projection_type = input()
rows = int(input())
cols = int(input())

ticket_price = 0

if projection_type == "Premiere":
    ticket_price = 12
elif projection_type == "Normal":
    ticket_price = 7.50
elif projection_type == "Discount":
    ticket_price = 5

all_seats = rows * cols
total_income = all_seats * ticket_price

print(f"{total_income:.2f} leva")
