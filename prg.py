# 6. Write a Python function to check whether a number falls within a given range.
def test_range(num):
    if num in range(1, 100):
        print(f"The number {num} is in given range ")
    else:
        print(f"The number {num} is not in given range")


test_range(103)