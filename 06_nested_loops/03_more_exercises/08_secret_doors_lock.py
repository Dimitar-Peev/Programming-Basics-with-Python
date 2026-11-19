upper_hundreds = int(input())
upper_tens = int(input())
upper_units = int(input())

for hundreds in range(1, upper_hundreds + 1):
    for tens in range(1, upper_tens + 1):
        for units in range(1, upper_units + 1):
            if hundreds % 2 == 0 and units % 2 == 0 and tens in (2, 3, 5, 7):
                print(f"{hundreds} {tens} {units}")