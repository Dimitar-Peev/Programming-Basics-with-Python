from math import ceil

height, width, unpainted_percent = int(input()), int(input()), int(input())

total_meters_for_painting = ceil(4 * height * width)
quadratic_meters_for_painting = total_meters_for_painting * (1 - unpainted_percent / 100)

while True:
    command = input()

    if command == "Tired!":
        print(f"{int(quadratic_meters_for_painting)} quadratic m left.")
        break

    paint_liters = int(command)
    quadratic_meters_for_painting -= paint_liters

    if quadratic_meters_for_painting <= 0:
        break

if quadratic_meters_for_painting == 0:
    print("All walls are painted! Great job, Pesho!")
elif quadratic_meters_for_painting < 0:
    print(f"All walls are painted and you have {int(abs(quadratic_meters_for_painting))} l paint left!")
