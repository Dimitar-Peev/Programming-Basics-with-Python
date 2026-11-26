hall_rent = int(input())

statues = hall_rent * 0.70
catering = statues * 0.85
sound = catering / 2

total = hall_rent + statues + catering + sound

print(f"{total:.2f}")