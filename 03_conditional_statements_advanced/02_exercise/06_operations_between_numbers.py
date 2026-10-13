n1 = int(input())
n2 = int(input())
operator = input()

if (operator == "/" or operator == "%") and n2 == 0:
    print(f"Cannot divide {n1} by zero")
else:
    result = 0.0

    if operator == '*':
        result = n1 * n2
    elif operator == '/':
        result = n1 / n2
    elif operator == '%':
        result = n1 % n2
    elif operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2

    if operator == '*' or operator == '-' or operator == '+':
        even_or_odd = "even"
        if result % 2 != 0:
            even_or_odd = "odd"
        print(f"{n1} {operator} {n2} = {result} - {even_or_odd}")
    elif operator == '/':
        print(f"{n1} {operator} {n2} = {result:.2f}")
    elif operator == '%':
        print(f"{n1} {operator} {n2} = {result}")
