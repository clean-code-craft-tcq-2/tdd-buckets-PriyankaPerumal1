from more_itertools import consecutive_groups


def get_group_count(readings, group):
    count = 0
    for item in group:
        count += readings.count(item)
    return count

def get_formatted_output(min, max, count):
    return "{}-{}, {}".format(min,max,count)

def get_frequent_range(readings):
    frequent_range = ""
    readings.sort()
    OrderedList = list(dict.fromkeys(readings))
    
    for group in consecutive_groups(OrderedList):
        group = list(group)
        if len(group) != 1:
            frequent_range += get_formatted_output(group[0],group[-1],get_group_count(readings,group)) + "\n"
    
    return frequent_range.rstrip()
