def functionName(arg1):
    print(arg1)
functionName("hello")

def sum(num1,num2):
    print(num1+num2)
sum(4,5)   

def sum(num1,num2):
    return num1+num2
print(sum(4,5)  ) 

def func(width,length):
    perimeter=2*(width+length)
    area = length*width
    print("Perimeter = ",perimeter)
    print("Area = ",area)

func(3,4)   #calling for hte function 
func(5,6)