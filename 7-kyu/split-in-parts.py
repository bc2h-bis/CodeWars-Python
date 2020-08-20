# The aim of this kata is to split a given string into different strings of equal size
# (note size of strings is passed to the method)

# Example:
# Split the below string into other strings of size #3
# 'supercalifragilisticexpialidocious'
# Will return a new string
# 'sup erc ali fra gil ist ice xpi ali doc iou s'

# Assumptions:
# String length is always greater than 0
# String has no spaces
# Size is always positive

def split_in_parts(s, part_length):
    # initialize empty list
    result = []
    # loop on the full length of string
    for c in range(0, len(s), part_length):
        # keep part and add it to the list
        result.append(s[c: c + part_length])
    # convert list to string
    return " ".join(result)


# Tests
print(split_in_parts("supercalifragilisticexpialidocious", 3))
print(split_in_parts("supercalifragilisticexpialidocious", 3)
      == "sup erc ali fra gil ist ice xpi ali doc iou s")
print(split_in_parts("HelloKata", 1) == "H e l l o K a t a")
print(split_in_parts("HelloKata", 9) == "HelloKata")

# Other soluces

# def split_in_parts(s, n):
#     return ' '.join([s[i:i+n] for i in range(0, len(s), n)])

# OR

# from textwrap import wrap
# def split_in_parts(s, part_length):
#     return " ".join(wrap(s,part_length))
