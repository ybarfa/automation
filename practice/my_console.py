# INPUT AND OUTPUT STATEMENT #

x = input("Enter First Number")
y = input("Enter Second Number")
i = int(x)
j = int(y)
print("The Sum:", i+j)

# ------------------------------------------------------------#


x = int(input("Enter First Number"))
y = int(input("Enter Second Number"))
print("The Sum:", x+y)

# ------------------------------------------------------------#
eno = int(input("Enter Employee No:"))
ename = input("Enter Employee Name:")
esal = float(input("Enter Employee Salary:"))
eaddr = input("Enter Employee Address:")
married = bool(input("Employee Maried ?[True|False]:"))
print("Please Confirm Information")
print("Employee No:", eno)
print("Employee Name:", ename)
print("Employee Salary:", esal)
print("Employee Address:", eaddr)
print("Employee Maried ?:", married)


# -----------------------------------------------------------#

a, b = [int(x)for x in input("Enter 2 Number:").split()]
print("Product Is:", a*b)

# ----------------------------------------------------------#

a, b, c = [float(x) for x in input("Enter 3 float Numbers:").split()]
print("The Sum Is:", a+b+c)
