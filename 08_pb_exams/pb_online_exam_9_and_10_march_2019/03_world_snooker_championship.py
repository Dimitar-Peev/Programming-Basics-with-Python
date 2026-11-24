stage = input()
ticket_type = input()
ticket_count = int(input())
photo = input()

price = 0

if stage == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
elif stage == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
elif stage == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400.00

total = price * ticket_count

if total > 4000:
    total = total * 0.75
    photo_cost = 0
elif total > 2500:
    total = total * 0.90
    if photo == 'Y':
        photo_cost = 40 * ticket_count
    else:
        photo_cost = 0
else:
    if photo == 'Y':
        photo_cost = 40 * ticket_count
    else:
        photo_cost = 0

total = total + photo_cost

print(f"{total:.2f}")