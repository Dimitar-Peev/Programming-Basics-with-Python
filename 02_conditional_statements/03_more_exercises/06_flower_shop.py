from math import floor, ceil

MAGNOLIA_PRICE = 3.25
HYACINTH_PRICE = 4.00
ROSE_PRICE = 3.50
CACTUS_PRICE = 8.00

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

total = magnolias * MAGNOLIA_PRICE + hyacinths * HYACINTH_PRICE + roses * ROSE_PRICE + cacti * CACTUS_PRICE
profit = total * 0.95

if profit >= gift_price:
    remaining = floor(profit - gift_price)
    print(f"She is left with {remaining} leva.")
else:
    needed = ceil(gift_price - profit)
    print(f"She will have to borrow {needed} leva.")
