# CONDITIONAL STATEMENT #
# 1  IF :-

name = input("enter name:")
if name == "Yash":
    print("Hello Yash Good Morning")
print("How Are You!!!")

# --------------------------------------------#

# 2 IF-ELSE :-

name = input("enter name:")
if name == "Yash Barfa":
    print("Hello Yash Good Morning")
else:
    print("Hello Guest Good Morning")
print("How Are You!!!")

# ------------------------------------------------#

# 3 IF-ELIF-ELSE :-

brand = input("enter your favourite brand:")
if brand == "RC":
    print("it is children brand")
elif brand == "KF":
    print("it is not that much kick")
elif brand == "FO":
    print("buy one get free one")
else:
    print("other brands are not recommended")

# -------------------------------------------------#

n = int(input("enter a digit from 0 to 9:"))
if n == 0:
    print("Zero")
elif n == 1:
    print("One")
elif n == 2:
    print("Two")
elif n == 3:
    print("Three")
elif n == 4:
    print("Four")
elif n == 5:
    print("Five")
elif n == 6:
    print("Six")
elif n == 7:
    print("Seven")
elif n == 8:
    print("Eight")
elif n == 9:
    print("Nine")
else:
    print("PLEASE ENTER A DIGIT FROM 0 TO 9")
