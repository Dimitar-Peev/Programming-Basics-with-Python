count = int(input())

total_tons = 0
total_cost = 0
bus_tons = 0
truck_tons = 0
train_tons = 0

for _ in range(count):
    tons = int(input())
    total_tons += tons

    if tons <= 3:
        total_cost += tons * 200
        bus_tons += tons
    elif tons <= 11:
        total_cost += tons * 175
        truck_tons += tons
    else:
        total_cost += tons * 120
        train_tons += tons

average_price = total_cost / total_tons
bus_percent = (bus_tons / total_tons) * 100
truck_percent = (truck_tons / total_tons) * 100
train_percent = (train_tons / total_tons) * 100

print(f"{average_price:.2f}")
print(f"{bus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")
