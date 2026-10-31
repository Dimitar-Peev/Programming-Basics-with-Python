tournaments = int(input())
starting_points = int(input())

total_points = starting_points
won_tournaments = 0
points_from_tournaments = 0

for _ in range(tournaments):
    stage = input()

    if stage == "W":
        total_points += 2000
        points_from_tournaments += 2000
        won_tournaments += 1
    elif stage == "F":
        total_points += 1200
        points_from_tournaments += 1200
    elif stage == "SF":
        total_points += 720
        points_from_tournaments += 720

average_points = points_from_tournaments // tournaments
win_percentage = won_tournaments / tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")