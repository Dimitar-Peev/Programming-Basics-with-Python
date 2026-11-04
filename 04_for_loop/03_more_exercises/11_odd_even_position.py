import sys

n = int(input())

odd_sum = 0.0
even_sum = 0.0

odd_min = sys.maxsize
odd_max = -sys.maxsize
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n + 1):
    number = float(input())

    if i % 2 == 1:
        odd_sum += number

        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number
    else:
        even_sum += number

        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number

print(f"OddSum={odd_sum:.2f},")

if odd_min == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")

if odd_max == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")

if even_min == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")

if even_max == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
