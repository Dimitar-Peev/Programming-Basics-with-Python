initial_hour = int(input())
initial_minutes = int(input())

hours_in_minutes = initial_hour * 60
total_time_minutes = hours_in_minutes + initial_minutes + 15

hour = total_time_minutes // 60
minutes = total_time_minutes % 60

if hour > 23:
    hour = 0

print(f"{hour}:{minutes:02d}")