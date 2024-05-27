# 1. Write a Python function to find the maximum of three numbers.
def max_num(num1, num2, num3):
    if (num1 > num2) and (num1> num3):
        return str("The Maximum number is: " + str(num1))
    elif ((num2 >= num1)and (num2>= num3)):
        return ("The Maximum Number is: "+ str(num2))
    else:
        return ("The Maximum Number is: "+ str(num3))

result = max_num(1,6,9)
print(result)