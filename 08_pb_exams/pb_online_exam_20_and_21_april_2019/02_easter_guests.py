from math import ceil

guests = int(input())
budget = int(input())

breads = ceil(guests / 3)
eggs = guests * 2

total = breads * 4 + eggs * 0.45

if budget >= total:
    left = budget - total
    print(f"Lyubo bought {breads} Easter bread and {eggs} eggs.")
    print(f"He has {left:.2f} lv. left.")
else:
    needed = total - budget
    print("Lyubo doesn't have enough money.")
    print(f"He needs {needed:.2f} lv. more.")
