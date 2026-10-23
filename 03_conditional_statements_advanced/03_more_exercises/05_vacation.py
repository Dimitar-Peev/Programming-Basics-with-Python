budget = float(input())
season = input()

location = ""
price = 0

if season == "Summer":
    location = "Alaska"
elif season == "Winter":
    location = "Morocco"

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        price = budget * 0.65
    elif season == "Winter":
        price = budget * 0.45
elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        price = budget * 0.80
    elif season == "Winter":
        price = budget * 0.60
else:
    accommodation = "Hotel"
    price = budget * 0.90

print(f"{location} - {accommodation} - {price:.2f}")
