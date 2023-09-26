# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
def count_upperlower(string):
    count = {"Uppercase": 0, "Lowercase": 0}
    for char in string:
        if char.isupper():
            count["Uppercase"] += 1
        elif char.islower():
            count["Lowercase"] += 1
    return count

result = count_upperlower('This is a sting')
print("Uppercase count:", result["Uppercase"])
print("Lowercase count:", result["Lowercase"])

 