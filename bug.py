def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}") #This will print 0 as expected

my_list = [10,20,30,40,50]
result = calculate_average(my_list)
print(f"Average: {result}") #This will print 30.0 as expected

my_list = [10,20,30,40,50, 'a']
result = calculate_average(my_list) # This will cause TypeError: unsupported operand type(s) for +: 'int' and 'str'