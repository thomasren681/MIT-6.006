import numpy as np

def Rod_Cutting(L,i):
    if i==0:
        return 0
    else:
        max_value = -float('inf')
        for p in range(1,i+1):
            max_value = max(max_value,L[p]+Rod_Cutting(L,i-p))
        return max_value


def Brute_Force(i):
    if i==1:
        return [[0],[1]]
    else:
        L_prime = Brute_Force(i-1)
        L_new = []
        for list in L_prime:
            L_new.append(list+[0])
            L_new.append(list+[1])

        return L_new

def Rod_Cutting_Brute_Force(L):
    All_Possible_cut = Brute_Force(len(L))
    Value_Sum = []
    for possible_cut in All_Possible_cut:
        value_sum = 0
        previous_cut = 0
        for ind, cut in enumerate(possible_cut):
            if cut == 1:
                value_sum += L[ind-previous_cut]
                previous_cut = ind

        Value_Sum.append(value_sum)

    max_sum = 0
    for sum in Value_Sum:
        max_sum = max(max_sum,sum)

    return max_sum



if __name__=='__main__':
    L = [0,1,10,13,18,20,31,32]
    print(Rod_Cutting(L,len(L)-1))
    print(Rod_Cutting_Brute_Force(L))
