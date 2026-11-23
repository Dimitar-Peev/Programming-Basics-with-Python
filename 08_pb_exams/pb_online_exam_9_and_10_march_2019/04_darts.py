player_name = input()

points = 301
successful_shots = 0
unsuccessful_shots = 0

command = input()

while "Retire" not in command:
    field = command
    score = int(input())
    shot = 0

    if field == "Single":
        shot = score
    elif field == "Double":
        shot = score * 2
    elif field == "Triple":
        shot = score * 3

    if shot <= points:
        points -= shot
        successful_shots += 1
    else:
        unsuccessful_shots += 1

    if points == 0:
        print(f"{player_name} won the leg with {successful_shots} shots.")
        break

    command = input()
else:
    print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")