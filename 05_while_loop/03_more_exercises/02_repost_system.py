target = int(input())

total = 0
cash_sum = 0
card_sum = 0
cash_count = 0
card_count = 0

is_cash = True
sum_is_enough = False
command = input()

while command != "End":
    price = int(command)

    if is_cash:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total += price
            cash_sum += price
            cash_count += 1
    else:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            total += price
            card_sum += price
            card_count += 1

    is_cash = not is_cash

    if total >= target:
        sum_is_enough = True
        break

    command = input()

if sum_is_enough:
    if cash_count > 0:
        avg_cash = cash_sum / cash_count
    else:
        avg_cash = 0

    if card_count > 0:
        avg_card = card_sum / card_count
    else:
        avg_card = 0

    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_card:.2f}")
else:
    print("Failed to collect required money for charity.")
