
values = [15, -4, 32, 0, -10, 25, 54, -200]

minimum_value = values[0]

for value in values[1:]:
    if value < minimum_value:
        minimum_value = value

print(f"Minimum value: {minimum_value}")