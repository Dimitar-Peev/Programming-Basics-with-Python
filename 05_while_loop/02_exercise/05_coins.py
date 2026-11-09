change = float(input())
total_sum = round(change * 100)

coin_count = 0

while total_sum > 0:

    if total_sum >= 200:
        total_sum -= 200
    elif total_sum >= 100:
        total_sum -= 100
    elif total_sum >= 50:
        total_sum -= 50
    elif total_sum >= 20:
        total_sum -= 20
    elif total_sum >= 10:
        total_sum -= 10
    elif total_sum >= 5:
        total_sum -= 5
    elif total_sum >= 2:
        total_sum -= 2
    else:
        total_sum -= 1

    coin_count += 1

print(coin_count)