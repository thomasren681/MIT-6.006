import random
import numpy as np

class Binary_Node:
    def __init__(self, x):
        self.item = x
        self.left = None
        self.right = None
        self.parent = None
        # self.subtree_update()     # used in lec 7

    def subtree_iter(self): # O(n)
        '''
        :return: traverse the whole tree to the traversal order
        '''
        if self.left:
            yield from self.left.subtree_iter()
        yield self
        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self):
        '''
        :return: the first node in the traversal order
        '''
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self):
        '''
        :return: the last node in the traversal order
        '''
        if self.right:
            return self.right.subtree_last()
        else:
            return self

    def successor(self):
        '''
        :return: the next node in traversal order i.e. the successor
        '''
        if self.right:
            return self.right.subtree_first()
        else:
            # return the lowest ancestor of <X> for which <X> is in its left subtree
            while self.parent and (self is self.parent.right):
                self = self.parent
            return self.parent

    def predecessor(self):
        '''
        :return: the previous node in traversal order i.e. the predecessor
        '''
        if self.left:
            return self.left.subtree_last()
        else:
            while self.parent and (self is self.parent.left):
                self = self.parent
            return self.parent

    def subtree_insert_before(self,new):
        # insert the new node in to the previous location in the traversal order
        if self.left:
            A = self.left.subtree_last()
            A.right, new.parent = new, A
        else:
            self.left, new.parent = new, self

    def subtree_insert_last(self, new):
        # insert the new node in to the next location in the traversal order
        if self.right:
            A = self.right.subtree_first()
            A.left, new.parent = new, A
        else:
            self.right, new.parent = new, self

    def subtree_delete(self):
        if self.left or self.right:
            # not a leaf
            if self.left:
                B = self.predecessor()
            else:
                B = self.successor()
            self.item, B.item = B.item, self.item
            return B.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None

        return self


class Binary_Tree():
    def __init__(self,Node_Type = Binary_Node):
        self.root = None
        self.size = 0
        self.Node_Type = Node_Type

    def __len__(self):
        return self.size
    def __iter__(self):
        if self.root:
            for A in self.root.subtree_iter():
                yield A.item

    def build(self, X):
        '''
        :param X: an array of items
        :return: a binary tree whose traversal order is the order of the input array
        '''
        A = [x for x in X]
        def build_subtree(A, i, j):
            '''
            :param A: a list data structure of the input array
            :param i: starting index
            :param j: ending index
            :return: the root of the sub binary tree
            '''
            c = (i+j)//2
            root = self.Node_Type(A[c])
            if i<c:
                # store items in the left subtree
                root.left = build_subtree(A,i,c-1)
                root.left.parent = root
            if j>c:
                root.right = build_subtree(A,c+1,j)
                root.right.parent = root
            return root
        self.root = build_subtree(A,0,len(A)-1)

    def tree_iter(self):
        node = self.root.subtree_first()
        while node:
            yield node
            node = node.successor()

