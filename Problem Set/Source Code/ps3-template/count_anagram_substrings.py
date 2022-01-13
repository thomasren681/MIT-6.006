def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    ##################
    # YOUR CODE HERE #
    ##################
    k = len(S[0])
    n = len(S)
    A = [0 for i in range(n)]
    substring_table = {}
    for i in range(len(T) - k + 1):  # O(|A|+k) = O(|A|)
        if i == 0:
            substring = T[:k]
        else:
            substring = substring[1:] + T[i + k - 1]
        frequency_table = build_frequency_table(substring)
        if frequency_table in substring_table:
            substring_table[frequency_table] += 1
        else:
            substring_table[frequency_table] = 1

    for index,s in enumerate(S):
        s_frequency_table = build_frequency_table(s)
        if s_frequency_table in substring_table:
            A[index] = substring_table[s_frequency_table]
        else:
            A[index] = 0


    return tuple(A)


def single_count_anagram_substring(A,B):
    '''
    :param A: a string
    :param B: a substring with length less than A
    :return: the number of anagram substring B in A
    '''
    k = len(B)
    substring_table = {}
    for i in range(len(A)-k+1):  # O(|A|+k) = O(|A|)
        if i == 0:
            substring = A[:k]
        else:
            substring = substring[1:]+A[i+k-1]
        frequency_table = build_frequency_table(substring)
        if frequency_table in substring_table:
            substring_table[frequency_table] += 1
        else:
            substring_table[frequency_table] = 1

    B_frequency_table = build_frequency_table(B)
    if B_frequency_table not in substring_table:
        print('There is no anagram substring of B in A')
        return 0
    else:
        return substring_table[B_frequency_table]




def build_frequency_table(str):
    '''
    :param str: a string
    :return: a tuple of frequency table of alphabets
    '''
    alphabet = [0 for i in range(26)]
    for letter in str:
        index = ord(letter) - 97
        alphabet[index] += 1

    return tuple(alphabet)



if __name__ == '__main__':
    pass