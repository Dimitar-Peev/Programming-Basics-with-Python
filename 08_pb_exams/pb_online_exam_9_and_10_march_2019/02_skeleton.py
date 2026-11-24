control_minutes = int(input())
control_seconds = int(input())
track_length = float(input())
seconds_per_100m = int(input())

control_total = control_minutes * 60 + control_seconds

time = (track_length / 100) * seconds_per_100m
time -= (track_length / 120) * 2.5

if time <= control_total:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time:.3f}.")
else:
    diff = time - control_total
    print(f"No, Marin failed! He was {diff:.3f} second slower.")