juniors = int(input())
seniors = int(input())
track = input()

junior_fee = 0.00
senior_fee = 0.00

if track == "trail":
    junior_fee = 5.50
    senior_fee = 7.00
elif track == "cross-country":
    junior_fee = 8.00
    senior_fee = 9.50
elif track == "downhill":
    junior_fee = 12.25
    senior_fee = 13.75
elif track == "road":
    junior_fee = 20.00
    senior_fee = 21.50

total = (juniors * junior_fee) + (seniors * senior_fee)

if track == "cross-country" and juniors + seniors >= 50:
    total *= 0.75

donation = total * 0.95

print(f"{donation:.2f}")