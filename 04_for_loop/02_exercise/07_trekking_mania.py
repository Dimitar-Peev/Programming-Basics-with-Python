groups = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for _ in range(groups):
    people = int(input())
    total_people += people

    if people <= 5:
        musala += people
    elif people <= 12:
        montblanc += people
    elif people <= 25:
        kilimanjaro += people
    elif people <= 40:
        k2 += people
    else:
        everest += people

print(f"{musala / total_people * 100:.2f}%")
print(f"{montblanc / total_people * 100:.2f}%")
print(f"{kilimanjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")
