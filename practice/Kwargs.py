
def person(name, **data):

    print(name)

    for i,j in data.items():
        print(i,j)

person('Yash',age=20, city='Indore', mob=9876543210)

