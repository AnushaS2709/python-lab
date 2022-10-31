rows=5
column=5
for i in range(1,rows+1):
    for j in range(1,column+1):
        if(i==1 or i==rows or j==1 or j==column):
           print('*',end='')
        else:
            print('*',end='')
    print()
