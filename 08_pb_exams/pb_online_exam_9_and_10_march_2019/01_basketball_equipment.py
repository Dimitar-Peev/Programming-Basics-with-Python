annual_fee = int(input())

shoes = annual_fee - (annual_fee * 0.40)
outfit = shoes - (shoes * 0.20)
ball = outfit / 4
accessories = ball / 5

total = annual_fee + shoes + outfit + ball + accessories

print(f"{total:.2f}")