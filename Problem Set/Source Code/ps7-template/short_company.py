import numpy as np

def argmax(A):
    '''
    :param A: a list of numbers or a string
    :return: i: the index of the largest item
    '''
    max = -float('inf')
    max_index = 0
    for i, item in enumerate(A):
        if item>max:
            max = item
            max_index = i

    return max_index

def LDS(A):
    '''
    :param A: a list of items that are comparable
    :return: the longest decreasing subsequence
    '''
    a = len(A)
    x = [1]*a
    y = [None]*a
    for i in reversed(range(a)):
        for j in range(i,a):
            if A[j]<A[i]:
                x[i] = max(x[i],1+x[j])
                if x[i] == 1+x[j]:
                    y[i] = j

    parent_pointer = argmax(x)
    Longest_Subseq = []
    while parent_pointer is not None:
        Longest_Subseq.append(A[parent_pointer])
        parent_pointer = y[parent_pointer]

    return Longest_Subseq

def LDS_short_company(p,n,k):
    '''
    :param p: nk prices in n contiguous days for a company
    :param n: number of days
    :param k: number of prices per day
    :return: LDS that doesn't skip days
    '''

    a = len(p)
    x = [1]*a
    y = [None]*a

    for i in reversed(range(n)):                        # O(nk^2)
        for j in reversed(range(i*k,k*(i+1))):          # O(k^2)
            for l in range(j,min((i+2)*k,n*k)):         # O(k)
                if p[l]<p[j]:
                    x[j] = max(x[j],1+x[l])
                    if x[j] == 1+x[l]:
                        y[j] = l

    parent_pointer = argmax(x)                          # O(nk)
    Longest_Subseq = []
    while parent_pointer is not None:                   # O(nk)
        Longest_Subseq.append(p[parent_pointer])
        parent_pointer = y[parent_pointer]

    return Longest_Subseq


def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    c = C[0]
    S = []
    ##################
    # YOUR CODE HERE #
    ##################
    C_lds = []
    C_subseq = []

    for p in P:                                 # O(snk^2)
        lds = LDS_short_company(p,n,k)          # O(nk^2)
        C_lds.append(len(lds))                  # O(1)
        C_subseq.append(lds)                    # O(1)

    c = C[argmax(C_lds)]                        # O(s)
    S = C_subseq[argmax(C_lds)]                 # O(s)

    return (c, S)


if __name__=='__main__':
    p = (52, 91, 86, 81, 1, 79, 64, 43, 32, 94, 42, 91, 9, 25, 73, 29, 31, 19, 70, 58, 12, 11, 41, 66, 63, 14, 39, 71, 38, 91)
    n = 10
    k = 3
    print(LDS_short_company(p,n,k))
