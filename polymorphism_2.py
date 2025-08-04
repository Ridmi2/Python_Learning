#method overloading


#in here we cannot call for 
# 2,3,4 as we only given two parameters . 
# how could we make it tobe effective 
# to both two parameter occasion and
#  three parameter  occasion

class Calc:
    def add(self,a,b):
        sum = a+b
        print(sum)

myObj =Calc()
myObj.add(2,3)        

#efffective method using polymorphism as a solution to method overloading
class Calc:
    def add (self,a=None,b=None,c=None):
        sum=0
        if a!=None and b!=None and c!=None:
            sum=a+b+c
            print(sum)

        elif a!=None and b!=None:
            sum=a+b
            print(sum)

        else:
            sum = a
            print(sum)
myObj = Calc()
myObj.add(2,5)             
