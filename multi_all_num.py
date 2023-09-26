# 3. Write a Python function to multiply all the numbers in a list.
def multiply(list):
    total = 1
    for i in list:
        total *= i
    return total
result = multiply([1,2,3,4])
print("The product of all elements is",result)
    