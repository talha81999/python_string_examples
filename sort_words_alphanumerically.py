def sorted_unique_words(input_string):
    # Split the input string into a list of words
    words = input_string.split(',')

    # Convert the list to a set to remove duplicates
    unique_words = set(words)

    # Sort the unique words alphanumerically
    sorted_words = sorted(unique_words)

    # Join the sorted words into a string with commas as separators
    result = ",".join(sorted_words)

    return result


# Accept a comma-separated sequence of words from the user
input_sequence = input("Enter a comma-separated sequence of words: ")

# Call the function and print the result
result = sorted_unique_words(input_sequence)
print("Distinct words in sorted form:", result)
