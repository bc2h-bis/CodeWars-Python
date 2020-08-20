# You are given a list of character sequences as a comma separated string.
# Write a function which returns another string containing all the character sequences
# except the first and the last ones, separated by spaces. If the input string is empty,
# or the removal of the first and last items would cause the string to be empty, return a null value.

def array(string):
    # convert string in list
    string_to_list = string.split(",")
    # remove first and last item
    remove_item = string_to_list[1:-1]
    # convert list in string
    result = " ".join(remove_item)
    # control string is not only spaces
    if result.isspace() is True or result == '':
        return None
    else:  # remove extremity space
        return result.strip()


# tests
print("Basic Tests")
print(array('') == None)
print(array(''))
print(array('1') == None)
print(array('1, 3') == None)
print(array('1,2,3') == '2')
print(array('1,2,3,4') == '2 3')
print(array('16,420,1') == '420')

# Other soluce
# def array(strng):
#     return ' '.join(strng.split(',')[1:-1]) or None
