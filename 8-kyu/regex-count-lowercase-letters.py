# Your task is simply to count the total number of lowercase letters in a string.

import re


def lowercase_count(string):
    # via regEx find and return specific matching characters
    match = re.findall("[a-z]", string)
    # count number of matching characters
    result = len(match)
    return(result)


    # test
print(lowercase_count("abcABC123"))
print(lowercase_count("abc") == 3)
print(lowercase_count("abcABC123") == 3)
print(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 3)
print(lowercase_count("") == 0)
print("@".islower())
