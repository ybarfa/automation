# PRINTING SQUARE PATTERN #

for i in range(4):
    for j in range(4):
        print("# ",end="")

    print()


# PRINTING TRIANGLE PATTERN #

for i in range(4):
    for j in range(i+1):
        print("# ",end="")

    print()

# PRINTING TRIANGLE PATTERN IN ANOTHER WAY #

for i in range(4):
    for j in range(4-i):
        print("# ",end="")

    print()