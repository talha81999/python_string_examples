"""
Write a Python program to remove characters that
have odd index values in a given string.
"""


def count_word_occurrence(text):
    char_count_dic = {}
    text = text.split(" ")
    for txt in text:
        if txt in char_count_dic:
            char_count_dic[txt] += 1
        else:
            char_count_dic[txt] = 1
    return char_count_dic


message = input("Enter a message: ")
print(count_word_occurrence(message))
