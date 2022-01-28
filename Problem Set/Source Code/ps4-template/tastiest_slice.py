from Set_AVL_Tree import BST_Node, Set_AVL_Tree
#######################################
# DO NOT REMOVE THIS IMPORT STATEMENT #
# DO NOT MODIFY IMPORTED CODE         #
#######################################
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
        if L[i][0]<=R[j][0]:
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
        if A[0][0]<=A[1][0]:
            return A
        else:
            return A[::-1]
    else:
        half = len(A)//2
        L = Merge_Sort(A[:half])
        R = Merge_Sort(A[half:])
        return merge(L,R)

class Key_Val_Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self): 
        return "%s,%s" % (self.key, self.val)

def prefix_sum(A):
    if A:
        return A.prefix_sum
    else:
        return int(0)

def max_prefix_sum(A):
    if A:
        return A.max_prefix_sum
    else:
        return -float('inf')

class Part_B_Node(BST_Node):


    def subtree_update(A):
        super().subtree_update()
        #########################################
        # ADD ANY NEW SUBTREE AUGMENTATION HERE #
        #########################################

        A.prefix_sum = A.item.val
        if A.left:
            A.prefix_sum += A.left.prefix_sum
        if A.right:
            A.prefix_sum += A.right.prefix_sum

        left, right = -float('inf'), -float('inf')
        middle = A.item.val

        if A.left:
            left = A.left.max_prefix_sum
            middle += A.left.prefix_sum
        if A.right:
            right = middle + A.right.max_prefix_sum
        A.max_prefix_sum = max(left,middle,right)
        if A.max_prefix_sum == left:
            A.max_prefix_key = A.left.max_prefix_key
        elif A.max_prefix_sum == middle:
            A.max_prefix_key = A.item.key
        else:
            A.max_prefix_key = A.right.max_prefix_key






class Part_B_Tree(Set_AVL_Tree):
    def __init__(self): 
        super().__init__(Part_B_Node)

    def max_prefix(self):
        '''
        Output: (k, s) | a key k stored in tree whose
                       | prefix sum s is maximum
        '''
        k, s = 0, 0
        ##################
        # YOUR CODE HERE #
        ##################

        k = self.root.max_prefix_key
        s = self.root.max_prefix_sum

        return (k, s)

def tastiest_slice(toppings):
    '''
    Input:  toppings | List of integer tuples (x,y,t) representing 
                     | a topping at (x,y) with tastiness t
    Output: tastiest | Tuple (X,Y,T) representing a tastiest slice 
                     | at (X,Y) with tastiness T
    '''
    B = Part_B_Tree()   # use data structure from part (b)
    X, Y, T = 0, 0, 0
    ##################
    # YOUR CODE HERE #
    ##################
    # C = Part_B_Tree()
    # X_kv_pair = []
    # Y_kv_pair = []
    # for i, item in enumerate(toppings):
    #     X_kv_pair.append(Key_Val_Item(key=item[0], val=item[2]))
    # B.build(X_kv_pair)
    # X,_ = B.max_prefix()
    # for i, item in enumerate(toppings):
    #     if item[0]<=X:
    #         Y_kv_pair.append(Key_Val_Item(key=item[1],val=item[2]))
    # C.build(Y_kv_pair)
    # Y,T = C.max_prefix()

    toppings = Merge_Sort(toppings)

    for topping in toppings:
        B.insert(Key_Val_Item(key=topping[1],val=topping[2]))
        (y,t) = B.max_prefix()
        if T<t:
            X,Y,T = topping[0],y,t

    return (X, Y, T)

if __name__=='__main__':
    # toppings = [(3, 11, 30), (-25, -8, 16), (-21, 6, 31), (-3, 20, -3), (-9, -22, 8), (-24, 19, -23), (-7, -20, 11), (7, 27, 29), (-14, 22, -24), (24, 21, 11), (-17, 12, -24), (16, -13, 28), (-26, -27, -3), (-1, 29, -4), (-16, -29, -19)]
    # print(tastiest_slice(toppings))
    toppings = [(-26, -27, -3), (-25, -8, 16), (-24, 19, -23), (-21, 6, 31)]
    B = Part_B_Tree()
    for topping in toppings:
        B.insert(Key_Val_Item(key=topping[1],val=topping[2]))
        (y,t) = B.max_prefix()
        print(y,t)
        print(B)

    print(B.root.right.max_prefix_sum)