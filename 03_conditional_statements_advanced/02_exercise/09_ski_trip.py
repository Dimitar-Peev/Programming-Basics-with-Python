days = int(input())
room_type = input()
review = input()

nights = days - 1
price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

total_price = price_per_night * nights

if room_type == "apartment":
    if nights < 10:
        total_price *= 0.7
    elif 10 <= nights <= 15:
        total_price *= 0.65
    elif nights > 15:
        total_price *= 0.5

elif room_type == "president apartment":
    if nights < 10:
        total_price *= 0.9
    elif 10 <= nights <= 15:
        total_price *= 0.85
    elif nights > 15:
        total_price *= 0.8

if review == "positive":
    total_price *= 1.25
elif review == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")
