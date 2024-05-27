# # Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(num):
    if num < 2:
        return False 
    for i in range(2, num):
        if num % i == 0:
            return False  # Found a divisor, not a prime number
    return True  # No divisors found, it's a prime number

user_input = int(input("Enter a number: "))
result = is_prime(user_input)

if result:
    print(f"{user_input} is prime")
else:
    print(f"{user_input} is not prime")

