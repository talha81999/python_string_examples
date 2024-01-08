"""
Write a Python program to remove characters
that have odd index values in a given string.
"""


def remove_character_at_odd_index(text):
    char_at_even_index = ""
    for i in range(len(text)):
        if i % 2 == 0:
            char_at_even_index += text[i]
    return char_at_even_index


message = input("Enter a message: ")
print(remove_character_at_odd_index(message))
