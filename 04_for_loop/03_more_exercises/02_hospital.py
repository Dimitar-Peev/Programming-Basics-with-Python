days = int(input())

doctors = 7
treated = 0
untreated = 0

for day in range(1, days + 1):
    if day % 3 == 0 and untreated > treated:
        doctors += 1

    patients = int(input())

    if patients <= doctors:
        treated += patients
    else:
        treated += doctors
        untreated += patients - doctors

print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")