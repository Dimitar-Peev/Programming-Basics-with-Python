start_first = int(input())
start_second = int(input())
diff_first = int(input())
diff_second = int(input())

end_first = start_first + diff_first
end_second = start_second + diff_second

for first in range(start_first, end_first + 1):
    for second in range(start_second, end_second + 1):
        is_first_prime = True
        is_second_prime = True

        for i in range(2, first):
            if first % i == 0:
                is_first_prime = False
                break

        for i in range(2, second):
            if second % i == 0:
                is_second_prime = False
                break

        if is_first_prime and is_second_prime:
            print(f"{first}{second}")