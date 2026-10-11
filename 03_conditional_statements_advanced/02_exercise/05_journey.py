budget = float(input())
season = input()

destination = ""
vacation_type = ""
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_type = "Camp"
        money_spent = budget * 0.3
    elif season == "winter":
        vacation_type = "Hotel"
        money_spent = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_type = "Camp"
        money_spent = budget * 0.4
    elif season == "winter":
        vacation_type = "Hotel"
        money_spent = budget * 0.8
else:
    destination = "Europe"
    vacation_type = "Hotel"
    money_spent = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {money_spent:.2f}")
