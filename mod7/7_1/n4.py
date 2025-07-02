def get_max_index(numbers):
    max_index = 0
    max_value = numbers[0] 

    for index, value in enumerate(numbers): 
        if value > max_value: 
            max_index = index
            max_value = value

    return max_index

numbers = [1, 2, 3, 4, 5]
print(get_max_index(numbers))  # Output: 5
numbers = [5, 4, 3, 2, 1]
print(get_max_index(numbers))  # Output: 1
numbers = [1, 3, 2, 5, 4]
print(get_max_index(numbers))  # Output: 4