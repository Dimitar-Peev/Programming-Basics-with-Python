first_name = input()
second_name = input()

first_points = 0
second_points = 0

first_card = input()

while "End of game" not in first_card:
    first_card = int(first_card)
    second_card = int(input())

    if first_card > second_card:
        first_points += first_card - second_card
    elif second_card > first_card:
        second_points += second_card - first_card
    else:
        print("Number wars!")
        first_card_war = int(input())
        second_card_war = int(input())

        if first_card_war > second_card_war:
            print(f"{first_name} is winner with {first_points} points")
        else:
            print(f"{second_name} is winner with {second_points} points")
        break

    first_card = input()
else:
    print(f"{first_name} has {first_points} points")
    print(f"{second_name} has {second_points} points")