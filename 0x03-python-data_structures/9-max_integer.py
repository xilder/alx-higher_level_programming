#!/usr/bin/python3
def max_integer(my_list=[]): 
    if len(my_list) > 0:
        max_int = my_list[0]
        for i in my_list:
            if max_int < i:
                max_int = i
        return max_int
    else:
        return None
