class Student:
    # Developed by yash for python demo
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def talk(self):
        print("Hello i am :", self.name)
        print("My age is :", self.age)
        print("My marks are :", self.marks)


myobj = Student("yash", 20, 75)
print(myobj.talk())


class Test:

    def __init__(self):
        print("Constructer exeuction")

    def m1(self):
        print("Method exeuction")


t1 = Test()
t2 = Test()
t3 = Test()
t1.m1()


class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.d


t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.c
print(t.__dict__)
