# ITERATIVE STATEMENTS #
#1 FOR LOOP :-
# To print character present in the given string :-

s="Yash Barfa"
for x in s:
    print(x)
#-----------------------------#
# To print characters present in string index wise :-

s=input("enter some string:")
i=0
for x in s:
    print("The character present at",i,"index is:",x)
    i=i+1
#-----------------------------#
# To print Hello ten times

for x in range(10):
    print("Hello")
#------------------------------#
# To display numbers from 0 to 10 :-

for x in range(11):
    print(x)
#------------------------------#
# To display odd numbers from 0 to 20 :-

for x in range(21):
    print(x%2!=0)
#--------------------------------#
# To display numbers from 10 to 1 in descending order

for x in range(10,0,-1):
    print(x)
#--------------------------------------------------------------------#