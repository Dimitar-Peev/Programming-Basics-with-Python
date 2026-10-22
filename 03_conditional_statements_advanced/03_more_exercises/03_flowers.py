chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

chrysanthemum_price = 0.00
rose_price = 0.00
tulip_price = 0.00

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

total = (chrysanthemums * chrysanthemum_price) + (roses * rose_price) + (tulips * tulip_price)

if holiday == "Y":
    total *= 1.15

if season == "Spring" and tulips > 7:
    total *= 0.95

if season == "Winter" and roses >= 10:
    total *= 0.90

if chrysanthemums + roses + tulips > 20:
    total *= 0.80

total += 2

print(f"{total:.2f}")
