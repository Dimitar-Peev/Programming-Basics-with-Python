x = float(input())
y = float(input())
h = float(input())

front_back_wall = 2 * (x * x) - (1.2 * 2)
side_walls = 2 * (x * y) - 2 * (1.5 * 1.5)
total_wall_area = front_back_wall + side_walls

green_paint = total_wall_area / 3.4

roof_rectangles = 2 * (x * y)
roof_triangles = 2 * (x * h / 2)
total_roof_area = roof_rectangles + roof_triangles

red_paint = total_roof_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")