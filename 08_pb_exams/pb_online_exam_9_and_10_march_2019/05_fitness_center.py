visitors = int(input())

back = 0
chest = 0
legs = 0
abs_count = 0
protein_shake = 0
protein_bar = 0

for _ in range(visitors):
    activity = input()

    if activity == "Back":
        back += 1
    elif activity == "Chest":
        chest += 1
    elif activity == "Legs":
        legs += 1
    elif activity == "Abs":
        abs_count += 1
    elif activity == "Protein shake":
        protein_shake += 1
    elif activity == "Protein bar":
        protein_bar += 1

work_out = back + chest + legs + abs_count
protein = protein_shake + protein_bar

work_out_percent = work_out / visitors * 100
protein_percent = protein / visitors * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{work_out_percent:.2f}% - work out")
print(f"{protein_percent:.2f}% - protein")