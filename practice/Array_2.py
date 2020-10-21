from array import *

arr = array('i', [])

n = int(input("Enter The Length Of The Array"))

for i in range(n):
    x = int(input("Enter The Next Value"))
    arr.append(x)


print(arr)

val = int(input("Enter The Value For Search"))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1

print(arr.index(val))
