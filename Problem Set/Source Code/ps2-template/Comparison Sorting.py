import numpy as np

def selection_sort(A):
    for i in range(len(A)-1,0,-1):
        m = i
        # find the largest value before i+1
        for j in range(i):
            if A[m]<A[j]:
                m = j
        # swap the largest value to i
        A[m],A[i] = A[i],A[m]

    return A

def insert(A,insert_value):
    '''
    :param A: a sorted list
    :param insert_value: the value where insertion sort should be sorting
    :return:
    '''
    if insert_value>A[len(A)-1]:
        A.insert(len(A),insert_value)
        return A
    else:
        for i in range(len(A)):
            if insert_value<A[i]:
                A.insert(i,insert_value)
                return A



def insertion_sort(A):
    # insertion sort recurrent version
    if len(A) == 2:
        if A[0]<=A[1]:
            return A
        else:
            return A[::-1]
    else:
        insert_value = A[len(A)-1]
        A = insertion_sort(A[:len(A)-1])
        insert(A,insert_value)
        return A

def merge(L,R):
    '''
    :param L: the left sorted list
    :param R: the right sorted list
    :return: a sorted list combining the left and right in increasing order
    '''
    Merged_list = []
    L_len = len(L)
    R_len = len(R)
    i,j = 0,0
    while i<L_len and j<R_len:
        if L[i]<=R[j]:
            Merged_list.append(L[i])
            i += 1
        else:
            Merged_list.append(R[j])
            j += 1
    if i == L_len:
        while j<R_len:
            Merged_list.append(R[j])
            j += 1
    else:
        while i<L_len:
            Merged_list.append(L[i])
            i += 1

    return Merged_list


def Merge_Sort(A):
    '''
    :param A: an unsorted list
    :return: a sorted version of A in increasing order
    '''

    if len(A) == 1:
        return A
    elif len(A) == 2:
        if A[0]<=A[1]:
            return A
        else:
            return A[::-1]
    else:
        half = len(A)//2
        L = Merge_Sort(A[:half])
        R = Merge_Sort(A[half:])
        return merge(L,R)

if __name__ == '__main__':
    # sub_array = list(np.arange(5))
    # insert(sub_array,2)
    # print(sub_array)

    A = list(np.random.randint(0,20,10))
    print(A)
    # print(selection_sort(A))
    # A = [10,3,6,8]
    print(insertion_sort(A))