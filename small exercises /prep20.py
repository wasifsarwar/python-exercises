def most_common_sickness(file):

    read_file = open(file, 'r')
    corona = int(read_file.readline())
    flu = int(read_file.readline())
    cold = int(read_file.readline())


    if (corona > flu) and (corona > cold):
        print('Coronavirus most common')
    elif (flu > corona) and (flu > cold):
        print('Flu most common')
    elif (cold > corona) and (cold > flu):
        print( 'Cold most common')
    else:
        print('There\'s a tie!')