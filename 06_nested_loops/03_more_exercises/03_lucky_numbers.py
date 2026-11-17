n = int(input())

for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                left_sum = first + second
                right_sum = third + fourth

                if left_sum == right_sum and n % left_sum == 0:
                    print(f"{first}{second}{third}{fourth}", end=" ")