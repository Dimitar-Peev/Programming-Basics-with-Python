length = int(input())
width = int(input())
height = int(input())
percent_accessories = float(input())

volume = length * width * height
total_liters = volume / 1000
accessories_space = total_liters * (percent_accessories / 100)
result = total_liters - accessories_space

print(result)