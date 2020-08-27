rec={}
n=int(input("enter number of students:"))
i=1
while i <=n:
    name=input("enter student name:")
    marks=input("enter % of marks of students:")
    rec[name]=marks
    i=i+1
print("name of students","\t","% of marks")
for x in rec:
    print("\t",x,"\t",rec[x])
