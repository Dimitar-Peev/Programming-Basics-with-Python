chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

price_chicken_menu = chicken_menu_count * 10.35
price_fish_menu = fish_menu_count * 12.4
price_vegetarian_menu = vegetarian_menu_count * 8.15

all_menu_sum = price_chicken_menu + price_fish_menu + price_vegetarian_menu
dessert_price = all_menu_sum * 0.20
delivery = 2.50

total_sum = all_menu_sum + dessert_price + delivery

print(total_sum)