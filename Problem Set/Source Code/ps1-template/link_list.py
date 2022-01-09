from Doubly_Linked_List_Seq import *
import numpy as np

##############################################################
##############################################################
##################Problem 1-2#################################
##############################################################
##############################################################
# a = list(np.arange(20))
# # print(a)
# # a.insert(3,4)
# # print(a)
# # a.pop(3)
# # print(a)
#
# def reverse(D,i,k):
#
#     if k<2:
#         return D
#
#     first_item = D.pop(i)
#     last_item = D.pop(i+k-2)
#
#     D.insert(i,last_item)
#     D.insert(i+k-1,first_item)
#
#     reverse(D,i+1,k-2)
#
# # reverse(a,3,5)
# # print(a)
#
# def move(D,i,k,j):
#     '''
#     :param D: The input data structure i.e. list in python
#     :param i: starting index
#     :param k: length of items to be moved
#     :param j: index to be moved in front of, j should not be in the range of the k items
#     :return: the D after moved
#     '''
#
#     # Base case
#     if k<1:
#         return D
#
#     # Inductive step
#     if i<j:
#         item = D.pop(i)
#         D.insert(j-1,item)
#
#         move(D,i,k-1,j)
#
#     else:
#         item = D.pop(i)
#         D.insert(j,item)
#
#         move(D,i+1,k-1,j+1)
#
# print(a)
# # move(a,3,3,8)
# move(a,8,3,3)
#
# print(a)


##############################################################
##############################################################
##################Problem 1-4#################################
##############################################################
##############################################################

DS = Doubly_Linked_List_Seq()
a = np.arange(10)
for i in a:
    DS.insert_first(i)
    DS.insert_last(i)
print(DS)
