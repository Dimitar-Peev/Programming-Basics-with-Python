budget = float(input())
video_count = int(input())
cpu_count = int(input())
ram_count = int(input())

VIDEO_CARD_PRICE = 250
CPU_DISCOUNT = 0.35
RAM_DISCOUNT = 0.1

video_sum = video_count * VIDEO_CARD_PRICE
cpu_sum = cpu_count * (video_sum * CPU_DISCOUNT)
ram_sum = ram_count * (video_sum * RAM_DISCOUNT)

total_sum = video_sum + cpu_sum + ram_sum

if video_count > cpu_count:
    total_sum = total_sum * 0.85

diff = abs(total_sum - budget)
if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
