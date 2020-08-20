# Write a comparator for a list of phonetic words for the letters of the greek alphabet.
# A comparator is:
# a custom comparison function of two arguments (iterable elements) which should return a negative, zero or positive
# number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument
# (source: https://docs.python.org/2/library/functions.html#sorted)
# The greek alphabet is preloded for you as greek_alphabet:

greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    # return word position in greek_alphabet
    # pos1 = greek_alphabet.index(lhs)
    # pos2 = greek_alphabet.index(rhs)
    # compare each count
    # result = pos1 - pos2
    # return result base on result condition
    # if result > 0;
    # return result
    return (greek_alphabet.index(lhs)) - (greek_alphabet.index(rhs))


# Tests
print(greek_comparator('alpha', 'beta'))
print(greek_comparator('alpha', 'beta') < 0)
print(greek_comparator('psi', 'psi') == 0)
print(greek_comparator('upsilon', 'rho') > 0)
