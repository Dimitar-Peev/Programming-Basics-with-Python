from math import floor, ceil

days = int(input())
food_left_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_g = float(input())

total_food_needed = days * (dog_food_kg + cat_food_kg + (turtle_food_g / 1000))

if food_left_kg >= total_food_needed:
    food_remained = floor(food_left_kg - total_food_needed)
    print(f"{food_remained} kilos of food left.")
else:
    food_needed = ceil(total_food_needed - food_left_kg)
    print(f"{food_needed} more kilos of food are needed.")