# Imports
import nltk
from nltk.tokenize import word_tokenize

# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Use NLTK's part-of-speech (POS) tagger to tag each word with its corresponding POS tag
pos_tags = nltk.pos_tag(words)

# Print the tagged words and their POS tags
print(pos_tags)

# Word Count independent of NLTK
text = input("Enter your text: ")
word_count = text.split()
print word_count()


#Counting words
string = "Python is awesome, isn't it?"
substring = "is"

count = string.count(substring)

# print count
print("The count is:", count)
