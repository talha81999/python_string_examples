"""
Write a Python program to change a given
string to a newly string where the first
and last chars have been exchanged.
"""

def swap_first_and_last_char(message):
    first_char = message[0]
    last_char = message[-1]
    message = last_char + message[1:-1] + first_char
    return message


text = input("Enter a message : ")
result = swap_first_and_last_char(text)
print(result)
