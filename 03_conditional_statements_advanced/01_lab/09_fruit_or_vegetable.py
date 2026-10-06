product = input()

fruit = product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes"
vegetable = product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot"

if fruit:
    print("fruit")
elif vegetable:
    print("vegetable")
else:
    print("unknown")
