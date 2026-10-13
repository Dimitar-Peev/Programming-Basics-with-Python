month = input()
nights = int(input())

apartment_price = 0
studio_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

total_studio = studio_price * nights
total_apartment = apartment_price * nights

if month == "May" or month == "October":
    if nights > 14:
        total_studio *= 0.7
    elif nights > 7:
        total_studio *= 0.95
elif month == "June" or month == "September":
    if nights > 14:
        total_studio *= 0.8

if nights > 14:
    total_apartment *= 0.9

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")
