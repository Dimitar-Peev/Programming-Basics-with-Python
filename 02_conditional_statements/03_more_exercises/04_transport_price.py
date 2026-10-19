distance = int(input())
time_of_day = input()

TAXI_START_PRICE = 0.70
TAXI_DAILY_RATE = 0.79
TAXI_NIGHT_RATE = 0.90
BUSS_PRICE = 0.09
TRAIN_PRICE = 0.06
BUSS_MIN_DISTANCE = 20
TRAIN_MIN_DISTANCE = 100

price = 0.00

if distance >= TRAIN_MIN_DISTANCE:
    price = distance * TRAIN_PRICE
elif distance >= BUSS_MIN_DISTANCE:
    price = distance * BUSS_PRICE
else:
    initial_fee = TAXI_START_PRICE
    if time_of_day == "day":
        price = initial_fee + (distance * TAXI_DAILY_RATE)
    else:
        price = initial_fee + (distance * TAXI_NIGHT_RATE)

print(f"{price:.2f}")
