import random
import numpy as np

from AVL_Tree    import AVL_Node, AVL_Tree

class key_value_pair():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return 'key: %s,value: %s'%(self.key,self.value)

class key_single():
    def __init__(self,key):
        self.key = key

    def __str__(self):
        return str(self.key)

class BST_Node(AVL_Node):
    def subtree_find(A, k):                # O(log n)
        if k < A.item.key:
            if A.left:  return A.left.subtree_find(k)
        elif k > A.item.key:
            if A.right: return A.right.subtree_find(k)
        else:           return A
        return None

    def subtree_find_next(A, k):           # O(log n)
        if A.item.key <= k:   
            if A.right: return A.right.subtree_find_next(k)
            else:       return None
        elif A.left:
            B = A.left.subtree_find_next(k)
            if B:       return B
        return A

    def subtree_find_prev(A, k):            # O(log n)
        if A.item.key >= k:   
            if A.left:  return A.left.subtree_find_prev(k)
            else:       return None
        elif A.right:
            B = A.right.subtree_find_prev(k)
            if B:       return B
        return A

    def subtree_insert(A, B):               # O(log n)
        if B.item.key < A.item.key:
            if A.left:  A.left.subtree_insert(B)
            else:       A.subtree_insert_before(B)
        elif B.item.key > A.item.key:
            if A.right: A.right.subtree_insert(B)
            else:       A.subtree_insert_after(B)
        else:    A.item = B.item

class Set_AVL_Tree(AVL_Tree):
    def __init__(self, Node_Type = BST_Node): 
        super().__init__(Node_Type)

    def iter_order(self): yield from self   # O(n)

    def build(self, A):                     # O(n log n)
        for x in A: self.insert(x)
        
    def find_min(self):                     # O(log n)
        if self.root:   return self.root.subtree_first().item

    def find_max(self):                     # O(log n)
        if self.root:   return self.root.subtree_last().item

    def find(self, k):                      # O(log n)
        if self.root:
            node = self.root.subtree_find(k)
            if node:    return node.item

    def find_next(self, k):                 # O(log n)
        if self.root:
            node = self.root.subtree_find_next(k)
            if node:    return node.item

    def find_prev(self, k):                 # O(log n)
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node:    return node.item

    def insert(self, x):                    # O(log n)
        new_node = self.Node_Type(x)
        if self.root:   
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False
        else:           
            self.root = new_node
        self.size += 1
        return True

    def delete(self, k):                    # O(log n)
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None:  self.root = None
        self.size -= 1
        return ext.item


if __name__=='__main__':
    np.random.seed(42)
    A = list(np.random.randint(-20,20,15))
    print(A)
    for i, item in enumerate(A):
        A[i] = key_value_pair(key=i,value=item)


    Set_AVL = Set_AVL_Tree()
    Set_AVL.build(A)
    print(Set_AVL)
    # first_node = Set_AVL.root.subtree_first()
    node = Set_AVL.root
    print(node.item)
    print(node.height)
    # for i in range(len(A)-1):
    #     node = node.successor()
    #     print(node.item)

    #########################################################
    # build a heap according to A
    # for i,item in enumerate(A):
    #     A[i] = AVL_Node(item)
    #
    # for i in range(len(A)):
    #     if i<(len(A)-1)//2:
    #         A[i].left = A[2*i+1]
    #         A[i].right = A[2*i+2]
    #     if i >= 0:
    #         A[i].parent = A[(i-1)//2]
    #########################################################

    # A = list(np.arange(0,20))
    # for i, item in enumerate(A):
    #     A[i] = key_single(key=item)
    #
    # AVL = Set_AVL_Tree()
    # AVL.build(A)
    # print(AVL)
