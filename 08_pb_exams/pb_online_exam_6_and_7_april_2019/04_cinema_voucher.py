voucher = int(input())

tickets = 0
others = 0

purchase = input()

while "End" != purchase:
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > voucher:
            break
        voucher -= price
        tickets += 1
    else:
        price = ord(purchase[0])
        if price > voucher:
            break
        voucher -= price
        others += 1

    purchase = input()

print(tickets)
print(others)
