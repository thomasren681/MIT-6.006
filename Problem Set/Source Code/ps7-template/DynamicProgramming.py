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

def LCS(A,B,i,j):
    # Subproblem for A[i:] and B[j:]
    if i == len(A) or j == len(B):
        return 0
    else:
        if A[i] == B[j]:
            return 1+LCS(A,B,i+1,j+1)
        else:
            return max(LCS(A,B,i,j+1),LCS(A,B,i+1,j))

def LIS(A):
    max_subseq = 1
    for j in range(len(A)):
        max_subseq = max(max_subseq,LIS_use_i(A,j))

    return max_subseq


def LIS_use_i(A,i):
    # The LIS that uses A[i] for sequence A[:i]
    if i == 0:
        return 1
    else:
        max_subseq = 1
        for j in range(i-1,-1,-1):
            if A[i]>A[j]:
                max_subseq = max(max_subseq,1+LIS_use_i(A,j))

        return max_subseq

def LDS(A):
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

if __name__=='__main__':


    #######################################
    # LCS test (Longest Common Subsequence)
    # A = 'hieroglyphology'
    # B = 'michaelangelo'
    # print(LCS(A,B,0,0))
    #######################################

    #######################################
    # LIS test (Longest Increasing Subsequence)
    # A = 'carbohydrate'
    # print(LIS(A))
    #######################################

    #######################################
    # LDS test (Longest Decreasing Subsequence)
    A = [2,3,5,4,6,3,2,1]
    print(LDS(A))
    #######################################

