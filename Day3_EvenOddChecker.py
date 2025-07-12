def check_odd_even(numbers):
    result = {}
    for num in numbers:
        if num % 2 == 0:
            result[num] = "Even"
        else:
            result[num] = "Odd"
    return result

# Example list of numbers
numbers_list = [3, 4, 7, 10, 13, 16, 19, 22]

# Call the function
result = check_odd_even(numbers_list)

# Print the result
for number, status in result.items():
    print(f"{number} is {status}")
