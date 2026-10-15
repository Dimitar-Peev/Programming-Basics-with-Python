vegetable_price_per_kg = float(input())
fruit_price_per_kg = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())

ONE_EURO = 1.94

vegetables_price_lv = vegetable_price_per_kg * vegetable_kg
fruits_price_lv = fruit_price_per_kg * fruit_kg
total_euro = (vegetables_price_lv + fruits_price_lv) / ONE_EURO

print(f"{total_euro:.2f}")
