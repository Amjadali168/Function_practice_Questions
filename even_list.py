#  Write a Python program to print the even numbers from a given list.
def even_num(lst):
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

result = even_num([1,3,5,7,8,6,2,4])
print("the list of even numbers is: ", result)