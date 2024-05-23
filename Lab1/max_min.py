numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Check if the list is empty
if not numbers:
    max_num = None
    min_num = None
else:
    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")
