def calculate_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

result = calculate_sum([1, 2, 3, 4])
print("The sum of the numbers is:", result)
