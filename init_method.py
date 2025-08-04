class Student:
   name = "Ridmi"
   age = 25

student1=Student()
print(student1.name)   

student2=Student()
print(student2.name)#both gives the same name .if you want to change the name with a mwthod you have to use init


#init method - calling for this method continusly after you create a object
class Student:
   def __init__(self):
      print("Hello")
st1 =Student()      
st2 =Student()#though wwe did not call for the method by object it calls automatically after create an object

#example-crate connection between attributes and methods
class Student:
   def __init__(self,name,age):
      self.name=name
      self.age =age
   
st1 =Student('Ridmi',23)      
st2 =Student('Hasitha',25)
print(st1.name)
print(st1.age)
print(st2.name)
print(st2.age)
