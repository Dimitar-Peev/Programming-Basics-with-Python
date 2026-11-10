bottles = int(input())

total_detergent = bottles * 750
remaining = total_detergent

dishes = 0
pots = 0
load_number = 0
not_enough = False

command = input()

while command != "End" and not not_enough:
    count = int(command)
    load_number += 1

    if load_number % 3 == 0:
        pots += count
        required = count * 15
    else:
        dishes += count
        required = count * 5

    if required > remaining:
        missing = required - remaining
        print(f"Not enough detergent, {missing} ml. more necessary!")
        not_enough = True
    else:
        remaining -= required
        command = input()

if not not_enough:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {remaining} ml.")