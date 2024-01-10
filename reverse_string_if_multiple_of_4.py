def reverse_string(text):
    text_length = len(text)
    if text_length % 4 == 0:
        text = text[::-1]
        return text
    else:
        return text


# for example, you can try a word food
message = input("Enter a message: ")
reverse_string = reverse_string(message)
print(reverse_string)
