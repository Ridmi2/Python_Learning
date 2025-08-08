for row in range (6):
    for col in range (7):
        if row==0 and col%3 !=0:
            print('* ', end='')
        elif row==1 and col%3==0:
            print ('* ', end='')
        elif row-col==2:
            print('* ', end='') 
        elif row+col==8:
            print('* ', end='')       
        else:
            print(' ', end='')
    print()