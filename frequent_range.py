def get_frequent_range(readings):
    readings.sort()
    frequent_range = f'{readings[0]}-{readings[-1]}, {len(readings)}'
    print(frequent_range)
    return frequent_range
