class Student:
    #Developed by yash for python demo
    def __init__(self, name, age, marks):
        self.name= name
        self.age= age
        self.marks= marks

    def talk(self):
        print("Hello i am :",self.name)
        print("My age is :",self.age)
        print("My marks are :",self.marks)


myobj = Student("yash", 20, 75)
print(myobj.talk())
