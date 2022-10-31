a=float(input('enter the value of a :'))
b=float(input('enter the value of b :'))
c=float(input('enter the value of c :'))
if((a>b)and (b>c)):
   print('a is greater')
elif((b>a) and (a>c)):
    print('b is greater')
else:
    print('c is greater')
