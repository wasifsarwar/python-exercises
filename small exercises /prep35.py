def get_highest_sum(list_of_values):
    list_max = 0
    for values in list_of_values:
        row_max = 0
        for i in range(1, len(values)):
            if (values[i] + values[i-1] > row_max):
                row_max = values[i] + values[i-1]
        if row_max > list_max:
            list_max = row_max
    return list_max