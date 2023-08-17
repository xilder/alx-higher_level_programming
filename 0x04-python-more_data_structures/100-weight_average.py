#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1 = 0
    denom = 0
    if my_list:
        for i in my_list:
            sum1 += i[0] * i[1]
            denom += i[1]
        return (sum1 / denom)
    return 0
