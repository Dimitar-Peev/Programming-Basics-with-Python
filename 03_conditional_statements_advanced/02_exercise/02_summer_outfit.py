degrees = int(input())
time_of_day = input()

outfit = ""
shoes = ""

cold = 10 <= degrees <= 18
warm = 18 < degrees <= 24
hot = degrees > 24

if time_of_day == "Morning":
    if cold:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif warm:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif hot:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if cold:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif warm:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif hot:
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif time_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
