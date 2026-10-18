v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipe1_total = p1 * h
pipe2_total = p2 * h
total_filled = pipe1_total + pipe2_total

if total_filled <= v:
    percent_full = (total_filled / v) * 100
    pipe1_percent = (pipe1_total / total_filled) * 100
    pipe2_percent = (pipe2_total / total_filled) * 100
    print(f"The pool is {percent_full:.2f}% full. Pipe 1: {pipe1_percent:.2f}%. Pipe 2: {pipe2_percent:.2f}%.")
else:
    overflow = total_filled - v
    print(f"For {h} hours the pool overflows with {overflow:.2f} liters.")