def exchange(Array, i, j):
    temp = Array[i]
    Array[i] = Array[j]
    Array[j] = temp

def Partition(Array,left_edge, right_edge, pivot):
    '''
    :param Array: an array within which we will do a partition
    :param left_edge: the starting index of the subarray we want to do partition
    :param right_edge: the ending index of the subarray we want to do partition
    :param pivot: the index of our assigned pivot
    :return: in-place Array being partitioned within the assigned indexes
    '''
    pivot_value = Array[pivot]
    exchange(Array,pivot, right_edge)
    boundary = left_edge-1
    for unxplored_index in range(left_edge,right_edge):
        if Array[unxplored_index] <= pivot_value:
            boundary += 1
            exchange(Array,boundary,unxplored_index)
    exchange(Array,boundary+1,right_edge)
    return boundary+1

if __name__=='__main__':
    A = [2,8,7,1,3,5,6,4]
    print(Partition(A,0,7,5))
    print(A)


