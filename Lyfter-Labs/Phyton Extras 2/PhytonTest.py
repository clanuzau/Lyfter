
from statistics import mean


my_values = [10, 20, 30, 40, 50, 60, 65, 70]

average_number = 0

numbers = [10, 20, 30, 40, 50, 65, 70]

average = sum(numbers) / len(numbers)

print(average)  # 40.714285714285715

average = mean(numbers)

print(average)
