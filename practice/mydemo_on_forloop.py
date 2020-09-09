# To print character present in the given string #

name="Yash Barfa"
for x in name:
     print(x)

# To print character present in string index wise #

s=input("enter some string")
i=0
for x in s:
      print("The character present at",i,"Index is:",x)
      i=i+1

# To print Hello 10 times #

for x in range(10):
     print("Hello")

# To display numbers from 0 to 10 #

for x in range(21):
     print(x)

# To display odd number from 0 to 20 #

for x in range(21):
     if(x%2!=0):
         print(x)

# To print sum of number present inside list #

list=eval(input("Enter list:"))
sum=0;
for x in list:
    sum=sum+x;
print("The Sum=",sum)