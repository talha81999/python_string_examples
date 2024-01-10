"""
Python function to convert a given string to all uppercase
if it contains at least 2 uppercase
characters in the first 4 characters.
"""


def convert_string_to_uppercase(text):
    """

    :rtype: str
    """
    if len(text) >= 4:
        uppercase_count = 0
        for i in range(4):
            if text[i].isupper():
                uppercase_count += 1
                if uppercase_count == 2:
                    text = text.upper()
                    break
        return text
    else:
        return "String length must be equal to or greater than 4"


"""
try out these strings
MEssage
MeSsage
MesSage
mESsage
MessAge
"""
message = input("Enter a message: ")
to_uppercase = convert_string_to_uppercase(message)
print(to_uppercase)
