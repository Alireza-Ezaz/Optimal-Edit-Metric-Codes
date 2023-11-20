import itertools

# This function generates all possible q-ary codewords of length n
def generate_codewords(n, q):
    alphabet = map(str, range(q))
    return [''.join(comb) for comb in itertools.product(alphabet, repeat=n)]


