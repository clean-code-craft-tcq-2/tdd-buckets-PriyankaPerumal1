from more_itertools import consecutive_groups

A2D = {
    '12Bit' : {'resolution' : 4094, 'maxCurrent' : 10, 'scalingFactor' : 0  },
    '10Bit' : {'resolution' : 1022, 'maxCurrent' : 30, 'scalingFactor' : 15 },
}

def get_group_count(readings, group):
    return sum([readings.count(item) for item in group])

def get_formatted_output(min, max, count):
    return "{}-{}, {}".format(min,max,count)

def get_frequent_range(readings):
    frequent_range = ""
    readings.sort()
    groups = consecutive_groups(list(dict.fromkeys(readings)))
    for group in groups:
        group = list(group)
        if len(group) != 1:
            frequent_range += get_formatted_output(group[0],group[-1],get_group_count(readings,group)) + "\n"
    
    return frequent_range.rstrip()

def ignore_error_readings(readings,type):
    return [reading for reading in readings if reading <= A2D[type]['resolution']]

def convert_input_to_amps(input, type):
    return abs(round((input * A2D[type]['maxCurrent'])/A2D[type]['resolution']) - A2D[type]['scalingFactor'])

def A2D_convertor(readings,type):
    return [convert_input_to_amps(reading,type) for reading in ignore_error_readings(readings,type)]
