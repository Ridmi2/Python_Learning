class myClass:
    x=10       #public variable
    __y=20     #private variable
myObj = myClass()
print(myObj.x)    #can access even from the out of the class
#print(myObj.__y)  #cannot access to a private varaible from the outside of a class


#how to access to a private variable by outside of a class
class myClass:
    x=10       #public variable
    __y=20     #private variable
    def disp(self):#create a method for private variable
        return self.__y
myObj = myClass()
 
print(myObj.disp())#calling for a method that include the private variable


#private methods
class myClass:
    def method(self):#public method
        print("Hello")
    def __method2(self):#private method
        print("welcome")
myObj1=myClass()
myObj1.method()  
myObj2=myClass()
#myObj2.__method2()    #give an ERROR  

#if we call for the private in the method we can gain it 
class myClass:
    def method(self):#public method
        print("Hello")
        self.__method2()
    def __method2(self):#private method
        print("welcome")
myObj1=myClass()
myObj1.method()  
