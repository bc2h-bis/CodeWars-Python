# Write a function that rearranges an integer into its largest possible value.
# super_size(123456) # 654321
# super_size(105)    # 510
# super_size(12)     # 21
# If the argument passed through is single digit or is already the maximum possible integer, your function should simply return it.

def super_size(n):
    string = str(n)
    results = ''.join(sorted(string, reverse=True))
    return int(results)


# tests
print(super_size(69))
print(super_size(69) == 96)
print(super_size(513) == 531)
print(super_size(1) == 1)
