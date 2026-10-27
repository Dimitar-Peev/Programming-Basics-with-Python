input_text = input()

letter_sum = 0

for vowel in input_text:
    if vowel == "a":
        letter_sum += 1
    if vowel == "e":
        letter_sum += 2
    if vowel == "i":
        letter_sum += 3
    if vowel == "o":
        letter_sum += 4
    if vowel == "u":
        letter_sum += 5

print(letter_sum)
