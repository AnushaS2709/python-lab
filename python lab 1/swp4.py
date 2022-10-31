# Write your code here :-)
a = 15
b = 26
print('before swapping a and b : '+ str(a)+'  ' +str(b))
a = a ^ b
b = a ^ b
a = a ^ b
print('after swapping a and b : ' + str(a)+'  '+str(b))
