def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle case with no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: 0

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: 30.0

my_list = [10, 20, 30, 40, 50, 'a']
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: 30.0

my_list = ['a', 'b', 'c']
result = calculate_average(my_list)
print(f"Average: {result}") # Output: Average: 0