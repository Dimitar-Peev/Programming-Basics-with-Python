count_tabs = int(input())
salary = int(input())

for _ in range(0, count_tabs):
    name_tab = input()

    if name_tab == "Facebook":
        salary -= 150
    elif name_tab == "Instagram":
        salary -= 100
    elif name_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        break

else:
    print(salary)
