def sort_words_alphanumerically(words):
    split_words = words.split(",")
    split_words = set(split_words)
    split_words = sorted(split_words)
    return split_words


comma_separated_words = input("Enter comma separated words: ")
sorted_words = sort_words_alphanumerically(comma_separated_words)
print(sorted_words)
