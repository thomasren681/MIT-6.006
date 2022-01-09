class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        '''
        :param x: an item (not a link list node)
        :return: a new link list with x to be the first node
        '''

        new_first_node = Doubly_Linked_List_Node(x)
        # if the link list is empty
        if self.head is None:
            self.head = new_first_node
            self.tail = new_first_node
        # the link list is not empty
        else:
            new_first_node.next = self.head
            self.head.prev = new_first_node
            self.head = new_first_node

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        new_last_node = Doubly_Linked_List_Node(x)

        # if the link list is empty
        if self.tail is None:
            self.head = new_last_node
            self.tail = new_last_node

        # if the link list is not empty
        else:
            new_last_node.prev = self.tail
            self.tail.next = new_last_node
            self.tail = new_last_node


    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        x = self.head.item
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        x = self.tail.item
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        L2.head = x1
        L2.tail = x2

        # connect the rest of the nodes into a new link list
        if x1 == self.head:
            self.head = x2.next
        else:
            x1.prev.next = x2.next

        if x2 == self.tail:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev

        # clear L2's head an tail
        x1.prev = None
        x2.next = None

        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        x1 = L2.head
        x2 = L2.tail
        # empty the L2
        L2.head = None
        L2.tail = None
        xn = x.next
        # reconstruct the new link list
        x1.prev = x
        x.next = x1

        x2.next = xn
        # if xn is the tail i.e. x is the last node in link list
        if xn is not None:
            xn.prev = x2
        else:
            self.tail = x2
