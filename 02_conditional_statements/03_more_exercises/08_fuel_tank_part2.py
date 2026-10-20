fuel_type = input()
fuel_amount = float(input())
has_card = input()

GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

GASOLINE_DISCOUNT = 0.18
DIESEL_DISCOUNT = 0.12
GAS_DISCOUNT = 0.08

price = 0.00

if fuel_type == "Gasoline":
    price = GASOLINE_PRICE
elif fuel_type == "Diesel":
    price = DIESEL_PRICE
elif fuel_type == "Gas":
    price = GAS_PRICE

if has_card == "Yes":
    if fuel_type == "Gasoline":
        price -= GASOLINE_DISCOUNT
    elif fuel_type == "Diesel":
        price -= DIESEL_DISCOUNT
    elif fuel_type == "Gas":
        price -= GAS_DISCOUNT

total = price * fuel_amount

if 20 <= fuel_amount <= 25:
    total *= 0.92
elif fuel_amount > 25:
    total *= 0.90

print(f"{total:.2f} lv.")
