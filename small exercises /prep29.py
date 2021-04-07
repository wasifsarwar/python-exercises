def sum_nums(items):
    total = 0
    for item in items:
        for number in item:
            if number < 10:
                total += number
    return total
