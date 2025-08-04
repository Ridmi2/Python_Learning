class Parent :
 def func1(self):
  print("hello")

class Child(Parent):
 def func2(self):
  print("Welcome")

myObj=Child()
myObj.func1()
myObj.func2()

#super function
class Parent :
 def func1(self):
  print("hello")

class Child(Parent):
 def func2(self):
  super().func1()
  print("Welcome")

myObj=Child()
#myObj.func1() #not want anymore
myObj.func2()

#method overriding
class Parent :
 def func1(self):
  print("hello")

class Child(Parent):
 def func2(self):
  print("Welcome")
 def func1(self):
  print("hi")

myObj=Child()
myObj.func1()


#another example
class Fruit:
 number_of_items =None
 unit_price =None
 def set_value(self,x,y):
  self.number_of_items=x
  self.unit_price =y

class Apple(Fruit):
 def price(self):
  print("For apple ",self.number_of_items*self.unit_price)  

class Orange(Fruit):
 def price(self):
  print("For orange ",self.number_of_items*self.unit_price) 

class Grapes(Fruit):
 def price(self):
  print("For grapes ",self.number_of_items*self.unit_price)   

myObj1 = Apple()
myObj2 = Orange()
myObj3 = Grapes()

myObj1.set_value(12,40)
myObj2.set_value(8,30)
myObj3.set_value(40,3)

myObj1.price()
myObj2.price()
myObj3.price()