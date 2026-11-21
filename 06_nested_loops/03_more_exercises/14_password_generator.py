n = int(input())
l = int(input())

for d1 in range(1, n + 1):
    for d2 in range(1, n + 1):
        for i1 in range(l):
            c1 = chr(ord('a') + i1)
            for i2 in range(l):
                c2 = chr(ord('a') + i2)
                for d3 in range(1, n + 1):
                    if d3 > d1 and d3 > d2:
                        print(f"{d1}{d2}{c1}{c2}{d3}", end=" ")
