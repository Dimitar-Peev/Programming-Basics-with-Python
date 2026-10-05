hour = int(input())
day = input()

is_closed = (hour < 10 or hour > 18) or day == "Sunday"
is_open = ((10 <= hour <= 18) and
           (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"))

if is_closed:
    print("closed")
elif is_open:
    print("open")
