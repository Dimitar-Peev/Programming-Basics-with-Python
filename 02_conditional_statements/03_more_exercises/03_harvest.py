from math import floor, ceil

area = int(input())
grapes_per_sqm = float(input())
needed_wine = int(input())
workers = int(input())

total_grapes = area * grapes_per_sqm
wine_grapes = total_grapes * 0.40
produced_wine = wine_grapes / 2.5

if produced_wine < needed_wine:
    shortage = floor(needed_wine - produced_wine)
    print(f"It will be a tough winter! More {shortage} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(produced_wine)} liters.")
    remaining = produced_wine - needed_wine
    per_person = remaining / workers
    print(f"{ceil(remaining)} liters left -> {ceil(per_person)} liters per person.")
