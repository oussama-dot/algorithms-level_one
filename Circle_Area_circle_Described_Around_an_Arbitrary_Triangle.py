import math
#input section
#start here -->
a = 5
b = 6
c = 7
#end here 
# varibales assiging -->
p = (a + b + c )/ 2
pi = 3.14159
#end here
# heron eqaion applyed -->
root =  math.sqrt(p *(p-a)*(p-b)*(p-c)) 
abc_sum = a * b * c
four_sum = 4 * root 
calc_one = abc_sum / four_sum
pow_of_calc = calc_one * calc_one
# ends here -->
#final area calculation 
area = pi * pow_of_calc
#ends here -->
#print 
print(area)
#programm end 