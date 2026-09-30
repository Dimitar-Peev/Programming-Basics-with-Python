PUZZLE_PRICE = 2.60
DOLL_PRICE = 3.00
BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

excursion = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price_for_puzzles = puzzles * PUZZLE_PRICE
price_for_dolls = dolls * DOLL_PRICE
price_for_bears = bears * BEAR_PRICE
price_for_minions = minions * MINION_PRICE
price_for_trucks = trucks * TRUCK_PRICE
sum_total = price_for_puzzles + price_for_dolls + price_for_bears + price_for_minions + price_for_trucks
sum_total = sum_total * 0.9

number_of_toys = puzzles + dolls + bears + minions + trucks

if number_of_toys >= 50:
    sum_total = sum_total * 0.75

difference = abs(sum_total - excursion)

if sum_total >= excursion:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")