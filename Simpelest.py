import itertools

# This function generates all possible q-ary codewords of length n
def generate_codewords(n, q):
    alphabet = map(str, range(q))
    # "itertools.product" creates Cartesian products of the given iterables (in this case, the alphabet),
    # and since the alphabet is a range from 0 to q−1, it generates the codewords in lexicographical order.
    return [''.join(comb) for comb in itertools.product(alphabet, repeat=n)]

# slide 13 of week 7 - This function computes the Edit distance between two given codewords using dynamic programming
def calculate_edit_distance(codeword1, codeword2):
    m, n = len(codeword1), len(codeword2)
    dp = [[0] * (n + 1) for k in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif codeword1[i - 1] == codeword2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # Deletion
                                   dp[i][j - 1],      # Insertion
                                   dp[i - 1][j - 1])  # Substitution
    return dp[m][n]

# This function checks if the given set of codewords is a valid code with minimum edit distance d between any two codewords
def is_code_valid(codewords, d):
    for i in range(len(codewords)):
        for j in range(i + 1, len(codewords)):
            if calculate_edit_distance(codewords[i], codewords[j]) < d:
                return False
    return True

# This function finds the optimal code of length n and size q with minimum edit distance d between any two codewords
# by exhaustively checking all possible sets of codewords
# we have to check the space of 2^(q^n) sets of codewords and for each set,
# we need to check the edit distance between every pair of codewords.
# In the worst case, this is choose(2, M) comparisons per set, where M is the maximum number of codewords in a set.
# Each comparison takes O(n*m) time, so the total time complexity is O(2^(q^n) * choose(2, M) * n*m).
# Therefore, the time complexity of this algorithm is O(2^(q^n) * choose(2, M) * n*m).
def find_optimal_code(n, q, d):
    all_codewords = generate_codewords(n, q)
    # initialize the optimal code to be the empty set
    optimal_code = set()
    for r in range(1, len(all_codewords) + 1):
        # "itertools.combinations" returns all possible combinations of the given iterable (in this case, the codewords)
        for codeword_set in itertools.combinations(all_codewords, r):
            if is_code_valid(codeword_set, d) and len(codeword_set) > len(optimal_code):
                optimal_code = codeword_set
    return optimal_code


print(generate_codewords(3, 3))
print(calculate_edit_distance("200", "1001"))
print(is_code_valid(["000", "111", "222"], 3))
print(find_optimal_code(4, 2, 2))