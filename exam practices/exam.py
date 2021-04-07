import random
def do_something(name, identifier, meters):
    original_name = name
    calculated = -10
    max_meters = 10.0
    i = 0
    while i < 100:
        #A
        print('identifier at A: ' + str(identifier))
        if meters > max_meters:
            meters = max_meters - 7.0
        if calculated > 50:
            name = 'Paul'

            #B
            identifier += 5
            print('meters at B: ' + str(meters))
        calculated += 5

        #C
        print(name, original_name, calculated, meters, identifier)
        meters += 1.0
        i+= 5

    #D
    print('calculated: ' +  str(calculated))


def calculate_grades(grades):
    max_grade = max(grades)
    min_grade = min(grades)
    grades.remove(max_grade)
    grades.remove(min_grade)

    sum_grades = 0
    for grade in grades:
        sum_grades += grade


    average = sum_grades/3
    return average
'''
grades = [100.0,80.0,82.0,90.0, 57.9]
result = calculate_grades(grades)
print(result)
'''

def do_something2(floats, number):
    result = 0
    for i in range(0,4):
        result += 2
        if floats[i] > 10.0:
            result += 2
        return result

print(do_something2([14.0,10.0, 12.3, 8.9,9.7,0.9, 122.4,12.0,14.0,3.0,18.0], 5))

def do_something1():
    r = random.randint(-10,5)
    q = random.randint(10,20)
    p = r - q
    result  = p + 30
    print('q:' + str(q))
    print('r:'+str(r))
    print('p:'+str(p))
    print('result:'+str(result))
#do_something1()