last_sector = input()
first_sector_rows = int(input())
odd_seats = int(input())

total_seats = 0
rows = first_sector_rows

for sector in range(ord('A'), ord(last_sector) + 1):
    sector_char = chr(sector)

    for row in range(1, rows + 1):
        if row % 2 != 0:
            seats = odd_seats
        else:
            seats = odd_seats + 2

        for seat in range(ord('a'), ord('a') + seats):
            print(f"{sector_char}{row}{chr(seat)}")
            total_seats += 1

    rows += 1

print(total_seats)