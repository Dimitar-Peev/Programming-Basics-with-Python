input_line = input()

prime_sum = 0
non_prime_sum = 0

while "stop" != input_line:
    current_num = int(input_line)

    if current_num < 0:
        print("Number is negative.")
        input_line = input()
        continue

    is_prime = True
    for i in range(2, int(current_num ** 0.5) + 1):
        if current_num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_sum += current_num
    else:
        non_prime_sum += current_num

    input_line = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
