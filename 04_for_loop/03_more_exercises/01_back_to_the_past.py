inherited_money = float(input())
target_year = int(input())

money_left = inherited_money
age = 18

for year in range(1800, target_year + 1):
    if year % 2 == 0:
        money_left -= 12000
    else:
        money_left -= 12000 + (50 * age)

    age += 1

if money_left >= 0:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    needed = abs(money_left)
    print(f"He will need {needed:.2f} dollars to survive.")