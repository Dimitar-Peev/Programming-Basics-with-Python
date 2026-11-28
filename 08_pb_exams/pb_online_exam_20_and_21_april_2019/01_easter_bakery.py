flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_packs = int(input())
yeast_packs = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.10
yeast_price = sugar_price * 0.20

total = flour_price * flour_kg
total += sugar_price * sugar_kg
total += eggs_price * eggs_packs
total += yeast_price * yeast_packs

print(f"{total:.2f}")