from array import *

vals=array('i',[5,9,8,4,2])

new_arr=array(vals.typecode, (a*a for a in vals))

for e in new_arr:
    print(e)