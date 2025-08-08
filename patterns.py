for i in range (5):
    for j in range (i+1):
        print('*', end='')
    print()

n=10
for i in range (n):
    for j in range (n-i):
        print('*', end='')
    print()    


#pyramid
for i in range (n):
    for j in range (n-i-1):
        print(' ', end='')
    for k in range (2*i+1):    
        print('*', end='')
    print()    