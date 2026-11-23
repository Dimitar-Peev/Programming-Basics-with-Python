tournaments = int(input())
start_points = int(input())

total_points = start_points
earned_points = 0
wins = 0

for _ in range(tournaments):
    stage = input()

    if stage == "W":
        total_points += 2000
        earned_points += 2000
        wins += 1
    elif stage == "F":
        total_points += 1200
        earned_points += 1200
    elif stage == "SF":
        total_points += 720
        earned_points += 720

average = earned_points // tournaments
win_percent = wins / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average}")
print(f"{win_percent:.2f}%")