import numpy as np
import collections


def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    list_count = []
    temp = 0
    increasing_count = 0
    for idx, item in enumerate(A):
        if item > temp:
            increasing_count += 1

        else:
            list_count.append(increasing_count)
            increasing_count = 1

        temp = item

    list_count.append(increasing_count) # get all the length of increasing subarrays

    max_num = np.max(np.array(list_count)) # find the maximum of subarrays' lengths
    dict = collections.Counter(list_count) # count numbers
    count = dict[max_num]
    ##################
    return count
