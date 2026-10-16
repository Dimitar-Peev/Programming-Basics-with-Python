mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = int(input())

bonito_price = mackerel_price * 1.60
horse_mackerel_price = sprat_price * 1.80
mussels_price = 7.50

total = bonito_price * bonito_kg + horse_mackerel_price * horse_mackerel_kg + mussels_price * mussels_kg

print(f"{total:.2f}")