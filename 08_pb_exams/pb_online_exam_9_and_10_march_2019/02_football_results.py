wins = 0
draws = 0
losses = 0

for _ in range(3):
    result = input()
    home_goals, away_goals = result.split(":")
    home_goals = int(home_goals)
    away_goals = int(away_goals)

    if home_goals > away_goals:
        wins += 1
    elif home_goals < away_goals:
        losses += 1
    else:
        draws += 1

print(f"Team won {wins} games.")
print(f"Team lost {losses} games.")
print(f"Drawn games: {draws}")