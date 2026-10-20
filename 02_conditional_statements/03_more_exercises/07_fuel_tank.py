fuel_type = input()
fuel_liters = float(input())

is_valid_fuel = fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas"

if not is_valid_fuel:
    print("Invalid fuel!")
else:
    if fuel_liters >= 25:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
