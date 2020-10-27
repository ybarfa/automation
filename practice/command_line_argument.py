# COMMAND LINE ARGUMENT #

from sys import argv
print("the number of command line argument:", len(argv))
print("the list of command line argument:", argv)
print("command line argument one by one:")
for x in argv:
    print(x)

# ------------------------------------------------------------#

from sys import argv
sum = 0
args = argv[1:]
for x in args:
    n = int(x)
    sum = sum+n
    print("the sum:", sum)
