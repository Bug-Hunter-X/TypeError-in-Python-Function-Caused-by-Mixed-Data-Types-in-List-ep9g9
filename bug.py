def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers) 
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will return 0

my_numbers_with_string = [10, 20, "thirty", 40, 50]
average_mixed = calculate_average(my_numbers_with_string) #this will cause an error
print(f"The average of a mixed list is: {average_mixed}")