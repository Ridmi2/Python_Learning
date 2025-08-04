a=int(input('Enter first number :'))
b=int(input('Enter second number :'))
#print(a/b) #if second nmuber =0 it gives an error without running bye also
print('Bye')

#so we have to use exception handling without stopping the code from s place where error occur without running other correct statemnt codes 
try:
    a=int(input('Enter first number :'))
    b=int(input('Enter second number :'))
    print(a/b) 
except:
    print('ZeroDivisionError')    
    print('Bye')


#if don't know the error type 
try:
    a=int(input('Enter first number :'))
    b=int(input('Enter second number :'))
    print(a/b) 
except Exception as e:
    print('Error',e)   
finally:     
    print('Bye') 