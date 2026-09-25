nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours_workers = int(input())

price_nylon = (nylon + 2) * 1.5
price_paint = (paint * 1.1) * 14.5
price_paint_thinner = paint_thinner * 5

sum_materials = price_nylon + price_paint + price_paint_thinner + 0.4
sum_workers = (sum_materials * 0.3) * hours_workers
total_sum = sum_materials + sum_workers

print(total_sum)
