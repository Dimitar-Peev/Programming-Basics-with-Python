moves = int(input())

score = 0.0

count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_50 = 0
count_invalid = 0

for _ in range(moves):
    number = int(input())

    if 0 <= number <= 9:
        score += number * 0.20
        count_0_9 += 1
    elif 10 <= number <= 19:
        score += number * 0.30
        count_10_19 += 1
    elif 20 <= number <= 29:
        score += number * 0.40
        count_20_29 += 1
    elif 30 <= number <= 39:
        score += 50
        count_30_39 += 1
    elif 40 <= number <= 50:
        score += 100
        count_40_50 += 1
    else:
        score /= 2
        count_invalid += 1

percent_0_9 = (count_0_9 / moves) * 100
percent_10_19 = (count_10_19 / moves) * 100
percent_20_29 = (count_20_29 / moves) * 100
percent_30_39 = (count_30_39 / moves) * 100
percent_40_50 = (count_40_50 / moves) * 100
percent_invalid = (count_invalid / moves) * 100

print(f"{score:.2f}")
print(f"From 0 to 9: {percent_0_9:.2f}%")
print(f"From 10 to 19: {percent_10_19:.2f}%")
print(f"From 20 to 29: {percent_20_29:.2f}%")
print(f"From 30 to 39: {percent_30_39:.2f}%")
print(f"From 40 to 50: {percent_40_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
