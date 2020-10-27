# Position Argument #

def person(name, age):
    print(name+' Barfa ')
    print(age-5)


person(age=20, name='Yash')

# Default Argument #


def person(name, age=18):
    print(name+' Barfa ')
    print(age)


person('Yash')

# Variable Length Argument #


def sum(a, *b):

    c = a

    for i in b:
        c = c+i

    print(c)


sum(5, 6, 34, 78, 89)
