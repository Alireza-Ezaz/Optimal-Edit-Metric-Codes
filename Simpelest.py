import itertools


# This function generates all possible q-ary codewords of length n
def generate_codewords(n, q):
    alphabet = map(str, range(q))
    # "itertools.product" creates Cartesian products of the given iterables (in this case, the alphabet),
    # and since the alphabet is a range from 0 to q−1, it generates the codewords in lexicographical order.
    return [''.join(comb) for comb in itertools.product(alphabet, repeat=n)]
