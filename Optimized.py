# We want to improve the efficiency of the brute force algorithm by using backtracking.
# week 5 slides give a good explanation of backtracking.
import itertools
import time
import math


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
                dp[i][j] = 1 + min(dp[i - 1][j],  # Deletion
                                   dp[i][j - 1],  # Insertion
                                   dp[i - 1][j - 1])  # Substitution
    return dp[m][n]

# This function checks if the new codeword can be added to the current set of codewords while maintaining the minimum edit distance d
def is_code_valid_after_addition_of_new_codeword(current_set, new_codeword, d):
    return all(calculate_edit_distance(new_codeword, cw) >= d for cw in current_set)

def is_starting_symbol_allowed_in_the_level(codeword, level, q):
    first_symbol = int(codeword[0])
    # We define thresholds for each symbol
    # result = math.ceil(M / q) + 1 as slides approach
    threshold_for_1 = 3  # symbol '1' is allowed from level 3 onwards
    threshold_for_2 = 5  # symbol '2' is allowed from level 5 onwards
    threshold_for_3 = 7  # symbol '3' is allowed from level 7 onwards

    if first_symbol == 1 and level < threshold_for_1:
        return False
    elif first_symbol == 2 and level < threshold_for_2:
        return False
    elif first_symbol == 3 and level < threshold_for_3:
        return False
    return True


# This is the basic backtracking algorithm that we discussed in class
def backtrack(codewords, n, q, d, M, current_set, optimal_set, level = 0):
    # If the current set reaches size M and is valid, update the optimal set
    if len(current_set) == M:
    # If the current set is a valid code with a larger size than the optimal code, we update the optimal code
        if len(current_set) > len(optimal_set[0]):
            optimal_set[0] = current_set.copy()
        return  # Stop further backtracking as we've reached the desired size

    for codeword in codewords:
        if is_code_valid_after_addition_of_new_codeword(current_set, codeword, d) and is_starting_symbol_allowed_in_the_level(codeword, level, q):
            # We add the codeword to the current set if it still satisfies the minimum edit distance d
            current_set.append(codeword)
            # We only need to consider codewords that come after the current codeword in the list
            codewords_for_next_level = codewords[codewords.index(codeword) + 1:]
            backtrack(codewords_for_next_level, n, q, d, M, current_set, optimal_set, level + 1)
            current_set.pop()


def find_optimal_code_with_backtracking(n, q, d, M):
    start_time = time.time()
    codewords = generate_codewords(n, q)  # Could be optimized for on-the-fly generation
    optimal_set = [[]]
    backtrack(codewords, n, q, d, M, [], optimal_set)
    end_time = time.time()
    return optimal_set[0], end_time - start_time

result = find_optimal_code_with_backtracking(5, 2, 2,9)
print(len(result[0]))
print(result[0])
print(result[1])
