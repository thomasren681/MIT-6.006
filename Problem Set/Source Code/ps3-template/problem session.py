import random
import numpy as np
from Linked_List_class import *

# Problem Session 3 -> Problem 3-1 Hash It Out
def Hash_Out(A, a, b, n):
    '''
    h(key) = (a*key+b) mod k
    :param A: a list of integer keys
    :param a: a in hash function h(key)
    :param b: b in hash function h(key)
    :param n: n in hash function h(key)
    :return: a hash table chaining with sequence i.e. list in Python
    '''
    HASH = [[] for i in range(n)]
    for item in A:
        new_item = (a*item+b)%n
        HASH[new_item].append(item)

    return HASH

def Hash_Out_double_modulo(A, a, b, c, n):
    '''
    h(key) = (a*key+b) mod n
    :param A: a list of integer keys
    :param a: a in hash function h(key)
    :param b: b in hash function h(key)
    :param c: c in hash function h(key)
    :param n: n in hash function h(key)
    :return: a hash table chaining with sequence i.e. list in Python
    '''
    HASH = [[] for i in range(n)]
    for item in A:
        new_item = (a*item+b)%c%n
        HASH[new_item].append(item)

    return HASH


# Problem Set 3 -> Problem 3-1
def Hash_Chaining_linked_list(A,a,b,n):
    '''
    :param A: a list of integer keys
    :param a: a in hash function h(key)
    :param b: b in hash function h(key)
    :param n: n in hash function h(key)
    :return: a hash table chaining with doubly linked list
    '''

    Hash_table = Hash_Out(A,a,b,n)
    chaining_hash_table = []
    for slot in Hash_table:
        # if slot is not None:
        chaining = Doubly_Linked_List_Seq()
        chaining.build(slot)
        chaining_hash_table.append(chaining.__str__())

    return chaining_hash_table

def collision(A,a,b,c,n):
    '''
    h(key) = (a*key+b) mod c mod n
    :param A: a list of integer keys
    :param a: a in hash function h(key)
    :param b: b in hash function h(key)
    :param c: c in hash function h(key)
    :param n: n in hash function h(key)
    :return: a boolean value tells whether a collision exists in our hash table
    '''
    Hash_table = Hash_Out_double_modulo(A,a,b,c,n)
    for slot in Hash_table:
        if len(slot)>1:
            print('collision exists for slot',slot)
            return False

    return True


def find_min_c(A,a,b,n):
    '''
    h(key) = (a*key+b) mod c mod n
    :param A: a list of integer keys
    :param a: a in hash function h(key)
    :param b: b in hash function h(key)
    :param n: n in hash function h(key)
    :return: c_min: the minimum value satisfying the non-collision situation
    '''
    c_min = n
    while True:
        if collision(A,a,b,c_min,n):
            print('The minimum c without causing collision is:',c_min)
            return c_min
        else:
            print('collision exists for c =',c_min)
            c_min += 1

def find_pair_sum(S,h):
    '''
    :param S: Whether there is a pair of values that sums to h
    :param h: the sum that to be searched
    :return: True if there exists a pair else False
    '''
    found = False
    for s_i in S:
        if h - s_i in S:
            print('Found s_j =', h - s_i, 's_i =', s_i)
            found = True
    if not found:
        print('There is no pair in set S sums to', h)

    return found

def find_max_leq(S,h):
    '''
    :param S: a sorted list
    :param h: for which the pair should be leq to
    :return: the max value of pair sum that is leq to h
    '''
    #
    for i in range(len(S)):
        if S[i] >= h:
            del S[i:]
            break
    i, j = 0, len(S) - 1
    t = 0 # use to store the best value
    while j - i > 1:
        pair_sum = S[i] + S[j]
        if pair_sum > h:
            j -= 1
        else:
            if pair_sum > t:
                t = pair_sum
            i += 1

    return t

if __name__ == '__main__':
    S = sorted(random.sample(range(1,1000),20))
    h = 476
    print(find_max_leq(S,h))







