import numpy as np

def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    B = []
    ##################
    # YOUR CODE HERE #
    ##################
    start_time = []
    terminate_time = []
    minimum_start_time = 0
    maximum_terminate_time = 0
    for (start,terminate) in R:             # O(n)
        start_time.append(start)
        terminate_time.append(terminate)
        if terminate>=maximum_terminate_time:
            maximum_terminate_time = terminate
        if start<=minimum_start_time:
            minimum_start_time = start

    time_span = maximum_terminate_time-minimum_start_time # O(1)
    booking_agenda = [0]*time_span

    for (start, terminate) in R:            # O(cn), for some constant c
        for i in range(start,terminate):    # O(1)
            booking_agenda[i] += 1

    start = minimum_start_time
    terminate = minimum_start_time + 1
    relative_time = 0
    i = 0

    while terminate<maximum_terminate_time: # O(1)
        if booking_agenda[start+relative_time] == booking_agenda[start+relative_time+1]:
            terminate += 1
            relative_time += 1
        else:
            relative_time = 0
            if booking_agenda[start+relative_time] != 0:
                B.append((booking_agenda[start+relative_time],start,terminate))
            start = terminate
            terminate += 1
    B.append((booking_agenda[start+relative_time],start,terminate))

    return tuple(B)

def merge_booking(B1,B2):
    '''
    :param B1: a booking schedule
    :param B2: a booking schedule
    :return: a booking schedule that merges the B1 and B2
    '''
    R1 = []
    R2 = []
    for num, start, terminate in B1:
        while num > 0:
            R1.append((start,terminate))
            num -= 1
    for num, start, terminate in B2:
        while num > 0:
            R2.append((start,terminate))
            num -= 1

    R = R1 + R2 # O(n)
    B = satisfying_booking(R)

    return B

if __name__ == '__main__':
    B1 = ((1,0,2),(3,2,3),(2,3,4),(3,4,6))
    B2 = ((3,0,1),(2,1,3),(4,3,6))
    print(merge_booking(B1,B2))
