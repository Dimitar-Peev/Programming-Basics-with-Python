destination = input()

while destination != "End":
    budget = float(input())
    saved = 0

    while saved < budget:
        amount = float(input())
        saved += amount

    print(f"Going to {destination}!")

    destination = input()