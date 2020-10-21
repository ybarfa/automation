
n1 = int(input("Enter First Number:"))
n2 = int(input("Enter Second Number:"))
n3 = int(input("Enter Third Number:"))

if n1 > n2 and n1 > n3:
    print("Biggest Number is:", n1)

elif n2 > n3:
    print("Biggest Number is:", n2)

else:
    print("Biggest Number is:", n3)

# ----------------------------END-----------------------------#

n = int(input("Enter Number:"))

if 1 <= n <= 10:
    print("The Number", n, "is in between 1 to 10")

else:
    print("The Number", n, "is not in between 1 to 10")

# ----------------------------END-----------------------------#

n = int(input("Enter a digit from 0 to 9:"))
if n == 0:
    print("ZERO")
elif n == 1:
    print("ONE")
elif n == 2:
    print("TWO")
elif n == 3:
    print("THREE")
elif n == 4:
    print("FOUR")
elif n == 5:
    print("FIVE")
elif n == 6:
    print("SIX")
elif n == 7:
    print("SEVEN")
elif n == 8:
    print("EIGHT")
elif n == 9:
    print("NINE")
else:
    print("PLEASE ENTER A DIGIT FROM 0 TO 9")

# --------------------------END-------------------------#
