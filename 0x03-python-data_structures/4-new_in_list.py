#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            duplicate_list = my_list.copy()
            duplicate_list[idx] = element
            return duplicate_list
