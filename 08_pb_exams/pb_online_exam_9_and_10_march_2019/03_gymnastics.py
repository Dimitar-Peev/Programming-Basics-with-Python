country = input()
apparatus = input()

total = 0

if country == "Russia":
    if apparatus == "ribbon":
        total = 9.100 + 9.400
    elif apparatus == "hoop":
        total = 9.300 + 9.800
    elif apparatus == "rope":
        total = 9.600 + 9.000
elif country == "Bulgaria":
    if apparatus == "ribbon":
        total = 9.600 + 9.400
    elif apparatus == "hoop":
        total = 9.550 + 9.750
    elif apparatus == "rope":
        total = 9.500 + 9.400
elif country == "Italy":
    if apparatus == "ribbon":
        total = 9.200 + 9.500
    elif apparatus == "hoop":
        total = 9.450 + 9.350
    elif apparatus == "rope":
        total = 9.700 + 9.150

percent = (20 - total) / 20 * 100

print(f"The team of {country} get {total:.3f} on {apparatus}.")
print(f"{percent:.2f}%")
