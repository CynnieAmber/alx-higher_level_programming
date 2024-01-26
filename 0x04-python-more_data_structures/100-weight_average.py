#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    elif not my_list:
        return 0
    elif my_list:
        total_ws = sum(score * weight for (score, weight) in my_list)
        total_w = sum(weight for (score, weight) in my_list)
        return total_ws/total_w
