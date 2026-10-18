rest_days = int(input())

game_minutes_per_year = 30000
minutes_for_game_in_working_day = 63
minutes_for_game_in_day_off = 127

work_days = 365 - rest_days
play_time = (work_days * minutes_for_game_in_working_day) + (rest_days * minutes_for_game_in_day_off)

difference = abs(play_time - game_minutes_per_year)
hours = difference // 60
minutes = difference % 60

if play_time > game_minutes_per_year:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
