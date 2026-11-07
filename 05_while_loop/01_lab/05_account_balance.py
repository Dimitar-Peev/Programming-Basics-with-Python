command = input()

total_money = 0
while "NoMoreMoney" != command:
    sum_income = float(command)

    if sum_income < 0:
        print('Invalid operation!')
        break

    total_money += sum_income
    print(f"Increase: {sum_income:.2f}")

    command = input()

print(f"Total: {total_money:.2f}")
