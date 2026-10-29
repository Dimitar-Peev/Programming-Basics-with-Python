age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_sum = 0

for current_age in range(1, age + 1):
    if current_age % 2 == 0:
        total_sum += ((current_age // 2) * 10) - 1
    else:
        total_sum += toy_price

difference = abs(total_sum - washing_machine_price)
if total_sum >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
