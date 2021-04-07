def count_calories(food):
    sum = 0
    for item in food:
        sum += food[item]
    return sum