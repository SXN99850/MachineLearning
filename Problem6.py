line_str = 'I am a teacher and I love to inspire and teach people'

# Use the split methods and set to get the unique words.
split_line_str = line_str.split(' ')
print("Line string after split", split_line_str)

# To get unique words, converting it to set as set does not accept repeated members
unique_words = set(split_line_str)
print("Unique words are", unique_words)

# How many unique words have been used in the sentence?
print("No. of unique words in given sentence are", len(unique_words))
