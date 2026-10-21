budget = float(input())
category = input()
people = int(input())

VIP_PRICE = 499.99
NORMAL_PRICE = 249.99

if 1 <= people <= 4:
    transport_percent = 0.75
elif people <= 9:
    transport_percent = 0.60
elif people <= 24:
    transport_percent = 0.50
elif people <= 49:
    transport_percent = 0.40
else:
    transport_percent = 0.25

transport_cost = budget * transport_percent
money_left = budget - transport_cost

ticket_price = 0

if category == "VIP":
    ticket_price = VIP_PRICE
elif category == "Normal":
    ticket_price = NORMAL_PRICE

tickets_cost = ticket_price * people

if money_left >= tickets_cost:
    remaining = money_left - tickets_cost
    print(f"Yes! You have {remaining:.2f} leva left.")
else:
    needed = tickets_cost - money_left
    print(f"Not enough money! You need {needed:.2f} leva.")
