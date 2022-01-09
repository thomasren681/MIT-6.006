import numpy as np


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


def special_damage(L,R):
    '''
    This function only satisfy the requirement of Problem 1-4 (c).
    For part (d) we will implement another function.
    :param L: the left sorted list
    :param R: the right sorted list
    :return: a sorted list containing the damage per house for every house
    '''

    L_len = len(L)
    R_len = len(R)
    Merged_list = [1]*(L_len+R_len)
    i,j = 0,0
    while i<L_len and j<R_len:
        if L[i]<=R[j]:
            Merged_list[i] += j
            i += 1
        else:
            j += 1
    if j==R_len:
        while i<L_len:
            Merged_list[i] += j
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

def get_damages(H):
    '''
    :param H: list of bricks per house
    :return: list of damage per house
    '''
    D = [1]*len(H)

    H2 = [(H[i],i) for i in range(len(H))]
############################################################
############################################################
    def get_special_damage(L, R):
        L_len = len(L)
        R_len = len(R)
        Merged_list = []
        i,j = 0,0
        while i<L_len and j<R_len:
            if L[i][0]<=R[j][0]:
                Merged_list.append(L[i])
                D[L[i][1]] += j
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
                D[L[i][1]] += j
                i += 1

        return Merged_list

############################################################
############################################################
    def merge_special_damage(H2):
        if len(H2) == 1:
            return H2
        elif len(H2) == 2:
            if H2[0][0] <= H2[1][0]:
                return H2
            else:
                D[H2[0][1]] += 1
                return H2[::-1]
        else:
            half = len(H2) // 2
            L = merge_special_damage(H2[:half])
            R = merge_special_damage(H2[half:])
            return get_special_damage(L, R)

############################################################
############################################################
    merge_special_damage(H2)

    return D


def get_damage_goofy(H):
    '''
    This is a goofy version of the get_damages func.
    This complexity doesn't satisfy the required big O complexity.
    But does the same thing, thus can be used as a sanity check.
    :param H:
    :return:
    '''
    D = []
    for i in range(len(H)):
        temp = np.sum(np.array(H[i:])<=H[i])
        D.append(temp)

    return D


if __name__ == '__main__':
    H = [34,57,70,19,48,2,94,7,63,75]
    print(get_damages(H))
    print(get_damage_goofy(H))