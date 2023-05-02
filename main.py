# Imports
import nltk
import csv
import english
from nltk.tokenize import word_tokenize

# Downloads
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Welcome
print("Welcome to The Word Farm...\n")
print("Here's a menu to help you choose your tool so you can farm you words.\n")

# Menu
while True:
    print("1/ Option 1")
    print("2/ Option 2")
    print("3/ Option 3")
    print("4/ Exit")
    choice = input("Which tool would you like to use?: ")
    
    if choice == "1":
        # code to execute for option 1
        print("Option 1 selected.")
    elif choice == "2":
        # code to execute for option 2
        print("Option 2 selected.")
    elif choice == "3":
        # code to execute for option 3
        print("Option 3 selected.")
    elif choice == "4":
        # exit the program
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

# Part of speech tagger

# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Use NLTK's part-of-speech (POS) tagger to tag each word with its corresponding POS tag
pos_tags = nltk.pos_tag(words)

# Print the tagged words and their POS tags
print(pos_tags)

# Word Spilt independent of NLTK
text = input("Enter your text: ")
word_split = text.split()
print("The split is:", word_split)


#Counting words
# string = "Python is awesome, isn't it?"
# substring = "is"

text_to_count = input("Enter a sentence: ")
substring = input("Enter substring")
count = text_to_count.count(substring)

# print count
print("The substring count is:", count)
