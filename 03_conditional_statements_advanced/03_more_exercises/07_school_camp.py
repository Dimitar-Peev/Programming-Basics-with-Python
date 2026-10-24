season = input()
group = input()
students = int(input())
nights = int(input())

price = 0
sport = ""

if season == "Winter":
    if group == "mixed":
        price = 10.00
    elif group == "girls" or group == "boys":
        price = 9.60
elif season == "Spring":
    if group == "mixed":
        price = 9.50
    elif group == "girls" or group == "boys":
        price = 7.20
elif season == "Summer":
    if group == "mixed":
        price = 20.00
    elif group == "girls" or group == "boys":
        price = 15.00

if season == "Winter":
    if group == "girls":
        sport = "Gymnastics"
    elif group == "boys":
        sport = "Judo"
    elif group == "mixed":
        sport = "Ski"
elif season == "Spring":
    if group == "girls":
        sport = "Athletics"
    elif group == "boys":
        sport = "Tennis"
    elif group == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if group == "girls":
        sport = "Volleyball"
    elif group == "boys":
        sport = "Football"
    elif group == "mixed":
        sport = "Swimming"

if students >= 50:
    discount = 0.50
elif students >= 20:
    discount = 0.15
elif students >= 10:
    discount = 0.05
else:
    discount = 0

total = price * students * nights
final_price = total * (1 - discount)

print(f"{sport} {final_price:.2f} lv.")
