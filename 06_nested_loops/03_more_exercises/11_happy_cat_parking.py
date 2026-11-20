days = int(input())
hours_per_day = int(input())

total = 0

for day in range(1, days + 1):
    day_total = 0

    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            day_total += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            day_total += 1.25
        else:
            day_total += 1

    total += day_total
    print(f"Day: {day} - {day_total:.2f} leva")

print(f"Total: {total:.2f} leva")
