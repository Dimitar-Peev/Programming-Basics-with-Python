needed_money = float(input())
owned_money = float(input())

count_spend_days = 0
count_total_days = 0
total_sum = owned_money

while total_sum < needed_money and count_spend_days < 5:

    action = input()
    amount = float(input())

    count_total_days += 1

    if action == "spend":
        total_sum -= amount
        count_spend_days += 1
        if total_sum < 0:
            total_sum = 0
    elif action == "save":
        count_spend_days = 0
        total_sum += amount

if count_spend_days == 5:
    print("You can't save the money.")
    print(count_total_days)

if total_sum >= needed_money:
    print(f"You saved the money for {count_total_days} days.")
