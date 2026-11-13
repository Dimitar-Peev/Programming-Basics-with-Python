hall_rent = int(input())

statuettes_price = hall_rent - (hall_rent * 0.30)
catering_price = statuettes_price - (statuettes_price * 0.15)
price_for_sound_system = catering_price / 2

total_sum = hall_rent + statuettes_price + catering_price + price_for_sound_system

print(f"{total_sum:.2f}")
