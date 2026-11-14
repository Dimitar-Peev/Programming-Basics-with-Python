stage_of_tournament = input()
ticket_type = input()
number_of_tickets = int(input())
trophy_photo = input()

ticket_price = 0

if stage_of_tournament == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
elif stage_of_tournament == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
elif stage_of_tournament == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400.00

total_price = ticket_price * number_of_tickets

if total_price > 4000:
    total_price -= total_price * 0.25
    trophy_photo = "N"
elif total_price > 2500:
    total_price -= total_price * 0.10

# total_price = total_price + (number_of_tickets * 40) if trophy_photo == "Y" else total_price

if trophy_photo == "Y":
    total_price = total_price + (number_of_tickets * 40)

print(f"{total_price:.2f}")
