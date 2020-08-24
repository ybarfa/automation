from sys import argv
print("the number of command line argument:",len(argv))
print("the list of command line argument:",argv)
print("command line argument one by one:")
for x in argv:
    print(x)