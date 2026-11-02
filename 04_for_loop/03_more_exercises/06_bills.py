months = int(input())

total_electricity = 0.0
total_water = 0.0
total_internet = 0.0
total_other = 0.0

for _ in range(months):
    electricity = float(input())

    water = 20.0
    internet = 15.0
    other = (electricity + water + internet) * 1.20

    total_electricity += electricity
    total_water += water
    total_internet += internet
    total_other += other

total_all = total_electricity + total_water + total_internet + total_other
average = total_all / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {average:.2f} lv")