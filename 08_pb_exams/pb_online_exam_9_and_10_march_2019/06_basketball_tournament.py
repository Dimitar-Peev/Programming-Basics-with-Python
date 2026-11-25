tournament = input()

total_games = 0
won_games = 0
lost_games = 0

while "End of tournaments" != tournament:
    games = int(input())

    for game_number in range(1, games + 1):
        desi_points = int(input())
        opponent_points = int(input())

        total_games += 1

        if desi_points > opponent_points:
            won_games += 1
            diff = desi_points - opponent_points
            print(f"Game {game_number} of tournament {tournament}: win with {diff} points.")
        else:
            lost_games += 1
            diff = opponent_points - desi_points
            print(f"Game {game_number} of tournament {tournament}: lost with {diff} points.")

    tournament = input()

won_percent = won_games / total_games * 100
lost_percent = lost_games / total_games * 100

print(f"{won_percent:.2f}% matches win")
print(f"{lost_percent:.2f}% matches lost")