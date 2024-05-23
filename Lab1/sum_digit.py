number = input("Enter a number: ")

total_sum = 0

for digit in number:
    total_sum += int(digit)

print(f"The sum of the digits of {number} is {total_sum}")
