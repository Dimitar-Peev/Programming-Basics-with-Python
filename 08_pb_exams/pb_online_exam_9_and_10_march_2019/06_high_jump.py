target = int(input())

bar = target - 30
jumps = 0
failed_at_height = 0
success = False

while bar <= target:
    failed = 0
    for _ in range(3):
        jump = int(input())
        jumps += 1

        if jump > bar:
            bar += 5
            break
        else:
            failed += 1

    if failed == 3:
        failed_at_height = bar
        break

    if bar > target:
        success = True
        break

if success:
    print(f"Tihomir succeeded, he jumped over {bar - 5}cm after {jumps} jumps.")
else:
    print(f"Tihomir failed at {failed_at_height}cm after {jumps} jumps.")