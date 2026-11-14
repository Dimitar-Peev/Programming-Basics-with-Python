record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

needed_time_to_climbing_all_distance = distance_in_meters * time_in_seconds_per_meter
additional_time = int(distance_in_meters / 50) * 30
total_needed_time_in_seconds = needed_time_to_climbing_all_distance + additional_time

if total_needed_time_in_seconds < record_in_seconds:
    print(f"Yes! The new record is {total_needed_time_in_seconds:.2f} seconds.")
else:
    difference = total_needed_time_in_seconds - record_in_seconds
    print(f"No! He was {difference:.2f} seconds slower.")
