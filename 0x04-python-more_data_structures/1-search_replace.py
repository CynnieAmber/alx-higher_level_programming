#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = []
    for ch in my_list:
        if ch == search:
            lst.append(replace)
            continue
        lst.append(ch)
    return lst
