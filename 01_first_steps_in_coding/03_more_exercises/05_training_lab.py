w = float(input())
h = float(input())

w_cm = w * 100
h_cm = h * 100

corridor = 100

seats_per_row = int(w_cm // 120)
rows = int((h_cm - corridor) // 70)

total_seats = (seats_per_row * rows) - 3

print(total_seats)