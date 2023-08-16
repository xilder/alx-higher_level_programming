#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def replacer(e):
        return e if e != search else replace
    return list(map(replacer, my_list))
