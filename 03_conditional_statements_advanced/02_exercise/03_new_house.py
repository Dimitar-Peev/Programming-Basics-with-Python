flower_type = input()
count = int(input())
budget = int(input())

price_per_flower = 0

if flower_type == "Roses":
    price_per_flower = 5
elif flower_type == "Dahlias":
    price_per_flower = 3.80
elif flower_type == "Tulips":
    price_per_flower = 2.80
elif flower_type == "Narcissus":
    price_per_flower = 3
elif flower_type == "Gladiolus":
    price_per_flower = 2.50

total_cost = count * price_per_flower

if flower_type == "Roses" and count > 80:
    total_cost *= 0.90
elif flower_type == "Dahlias" and count > 90:
    total_cost *= 0.85
elif flower_type == "Tulips" and count > 80:
    total_cost *= 0.85
elif flower_type == "Narcissus" and count < 120:
    total_cost *= 1.15
elif flower_type == "Gladiolus" and count < 80:
    total_cost *= 1.20

money = abs(budget - total_cost)
if budget >= total_cost:
    print(f"Hey, you have a great garden with {count} {flower_type} and {money:.2f} leva left.")
else:
    print(f"Not enough money, you need {money:.2f} leva more.")
