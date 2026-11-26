movie = input()
hall = input()
tickets = int(input())

price = 0

if movie == "A Star Is Born":
    if hall == "normal":
        price = 7.50
    elif hall == "luxury":
        price = 10.50
    elif hall == "ultra luxury":
        price = 13.50
elif movie == "Bohemian Rhapsody":
    if hall == "normal":
        price = 7.35
    elif hall == "luxury":
        price = 9.45
    elif hall == "ultra luxury":
        price = 12.75
elif movie == "Green Book":
    if hall == "normal":
        price = 8.15
    elif hall == "luxury":
        price = 10.25
    elif hall == "ultra luxury":
        price = 13.25
elif movie == "The Favourite":
    if hall == "normal":
        price = 8.75
    elif hall == "luxury":
        price = 11.55
    elif hall == "ultra luxury":
        price = 13.95

income = price * tickets

print(f"{movie} -> {income:.2f} lv.")