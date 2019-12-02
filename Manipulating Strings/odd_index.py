"""
Odd index :

Write a Python program to remove the characters which have odd index values of a given string.
"""


def remove_odd_index(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result = result + str[i]
    return result


print("Lets remove those pesky odd indexes!")
string = input("Give me a string: ")
print("Here's your new string: " + remove_odd_index(string))
