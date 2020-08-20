# https://www.codewars.com/kata/595970246c9b8fa0a8000086
# Your coworker was supposed to write a simple helper function to capitalize a string (that contains a single word) before they went on vacation.
# Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).
# Don't worry about numbers, special characters, or non-string types being passed to the function. The string lengths will be from 1 character up to 10 characters, but will never be empty.

def capitalize_word(word):
    return word.capitalize()

# def capitalize_word(word):
    # store the first letter
    # put the first letter capitalized
    # first_letter = word[0].upper()
    # store the word minus first letter
    # other_letters = word[1:]
    # concatenate first letter stored with the rest
    # concatenation = first_letter + other_letters
    # return concatenation


print(capitalize_word('word') == 'Word')
print(capitalize_word('i') == 'I')
print(capitalize_word('glasswear') == 'Glasswear')
print(capitalize_word('test encore') == 'Test encore')
