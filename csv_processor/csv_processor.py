##
### Description: This program reads in a CSV file with no column labels,
###              and can compute a maximum, minimum of a column. It also calculates
###              the average of a single column
###

def main():

    #prompt the user for csv file and read it
    filename = input("Enter CSV file name: \n")
    f = open(filename, "r")
    data = f.readlines()

    #2d list of lists of values read from csv file
    list_of_values = []

    for line in data:
       #split the rows into list and convert the values to float
        split = line.split(",")
        temp_list = []
        for value in split:
            value = float(value)
            temp_list.append(value)

        #add the list to 2d list
        list_of_values.append(temp_list)

    #prompt the user for column number
    column = int(input("Enter column number: \n"))

    #prompt the user for operation
    operation = input("Enter column operation: \n")

    if(operation == "min"):
        minimum(list_of_values, column)
    elif(operation == "max"):
        maximum(list_of_values, column)
    elif(operation == "avg"):
        average(list_of_values, column)
    else:
        print("invalid operation")



#this function calculates the minimum of a user prompted column
def minimum(list_of_values, column):

    #setting min_value to a really high number
    min_value = 100000000.0

    #loop over all the lists in 2d list
    for row in list_of_values:

        # checks elements in a certain column for each row
        # compares with min_value to see if element is the min
        if(row[column - 1] < min_value):
            min_value = row[column - 1]

    print("The minimum value in column", column, "is:", min_value)

#this function calculates the maximum of a user prompted column
def maximum(list_of_values, column):

    #setting min_value to 0.0
    max_value = 0.0

    #loop over all the lists in 2d list
    for row in list_of_values:

        # checks elements in a certain column for each row
        # compares with max_value to see if element is the max_value
        if(row[column - 1] > max_value):
            max_value = row[column - 1]

    print("The maximum value in column", column, "is:", max_value)

#this function calculates the average of a user prompted column
def average(list_of_values, column):

    sum_of_column = 0
    n = 0

    # sums the values in each column and checks number of elements
    # in that column to find the average
    for row in list_of_values:
        sum_of_column += row[column - 1]
        n += 1

    avg = sum_of_column / n
    print("The average for column", column, "is:", avg)

main()