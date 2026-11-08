goal = 10000
steps = 0

while steps < goal:
    command = input()

    if command == "Going home":
        final_steps = int(input())
        steps += final_steps
        break

    steps += int(command)

if steps >= goal:
    print("Goal reached! Good job!")
    print(f"{steps - goal} steps over the goal!")
else:
    print(f"{goal - steps} more steps to reach goal.")