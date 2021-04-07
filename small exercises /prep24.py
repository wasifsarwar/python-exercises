def get_gpa(grades):
    sum = 0
    for grade in grades:
        if grade == 'cs245' or grade == 'cs210' or grade == 'cs120':
            sum += grades[grade]

    return sum/3