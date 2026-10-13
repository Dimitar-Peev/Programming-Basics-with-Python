exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_minutes = (exam_hour * 60) + exam_minutes
arrival_time_minutes = (arrival_hour * 60) + arrival_minutes

diff_minutes = exam_time_minutes - arrival_time_minutes

if 0 <= diff_minutes <= 30:
    output = "On time"
elif diff_minutes > 30:
    output = "Early"
else:
    output = "Late"

print(output)

if diff_minutes < 0:
    arrival_period = "after"
else:
    arrival_period = "before"

diff_minutes = abs(diff_minutes)

if diff_minutes != 0:
    if diff_minutes < 60:
        print(f"{diff_minutes} minutes {arrival_period} the start")
    else:
        hour = diff_minutes // 60
        minutes = diff_minutes % 60
        print(f"{hour}:{minutes:02d} hours {arrival_period} the start")
