from math import floor, ceil

price_racket = float(input())
count_rackets = int(input())
count_shoes = int(input())

rackets_total = price_racket * count_rackets
shoes_price = price_racket / 6
shoes_total = shoes_price * count_shoes
equipment = (rackets_total + shoes_total) * 0.20

total = rackets_total + shoes_total + equipment

djokovic_pays = floor(total / 8)
sponsors_pay = ceil((total * 7) / 8)

print(f"Price to be paid by Djokovic {djokovic_pays:.0f}")
print(f"Price to be paid by sponsors {sponsors_pay:.0f}")