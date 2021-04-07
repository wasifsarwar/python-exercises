def copy_and_increment(integers):
    other = []
    for i in range(len(integers)):
        item = integers[i] + 1
        other.insert(i,item)
    return other