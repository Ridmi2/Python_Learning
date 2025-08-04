#method overriding

class Parent:
 x=40
class Child(Parent):
    x=50                  #output is 50 , 40 of paren class override by 50 of child class
    

myObj = Child()
print(myObj.x)