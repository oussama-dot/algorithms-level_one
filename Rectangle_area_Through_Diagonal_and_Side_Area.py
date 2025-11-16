import math
a = int(input("a"))
d = int(input("d"))

root_a = a * a 
root_d = d * d 
if root_a < root_d :
    area = (root_d - root_a)
else :
    area = (root_a - root_d)

root = math.sqrt(area)
res =  a*root
print (res)


