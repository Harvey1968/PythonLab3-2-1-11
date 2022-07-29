#3.2.1.11 LAB: The continue statement - the Pretty Vowel Eater

# Prompts the user to enter a word
print('"Why hello human I am the Pretty Vowel Eater, can you help me out?"')
# Creates the 'word_without_vowels' variable.
word_without_vowels = ""
# Assigns user input to the 'user_word' variable.
user_word = input("Please enter a word: ")
# Returns a string where all Characters are in upper case. Symbols and Numbers are ignored. 
user_word = user_word.upper()

# A 'for' loop that skips certain Characters entered by user
print('\n"ooooo that was yummy thanks!"\n"I don\'t need these though please have them back:"')
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        # Adds 'letter' value and the 'word_without_vowels' variable and assigns the result to the 'word_without_vowels' variable.
        word_without_vowels += letter
# The 'word_without_vowels' variable is then output on one line
print(word_without_vowels, "\n")



