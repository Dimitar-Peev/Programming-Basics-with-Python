movies_count = int(input())

best_movie = ""
best_rating = 0
worst_movie = ""
worst_rating = 11
total_rating = 0

for _ in range(movies_count):
    movie_name = input()
    rating = float(input())

    if rating > best_rating:
        best_rating = rating
        best_movie = movie_name

    if rating < worst_rating:
        worst_rating = rating
        worst_movie = movie_name

    total_rating += rating

average_rating = total_rating / movies_count

print(f"{best_movie} is with highest rating: {best_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {worst_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")