#single level inheritance

class Phone1:  #parent class
    def feature1(self):
        print("camera")
class Phone2(Phone1):
    def feature2(self):  #child class
        print("internet")

myObj = Phone2()
myObj.feature1()            

#mutiplw inheritance

class Phone1:  #parent class
    def feature1(self):
        print("camera")

class Phone3:  #parent class
    def feature3(self):
        print("blutooth")

class Phone2(Phone1,Phone3):
    def feature2(self):  #child class
        print("internet")

myObj = Phone2()
myObj.feature3()   

#multilevel inheritance
class Phone1:  #parent class
    def feature1(self):
        print("camera")

class Phone3(Phone1):  #parent class
    def feature3(self):
        print("blutooth")

class Phone2(Phone3):
    def feature2(self):  #child class
        print("internet")

myObj = Phone2()
myObj.feature3()
myObj.feature1()
myObj.feature2()
myObj = Phone3()
myObj.feature1()
myObj.feature2()#give an error
myObj.feature3()
myObj = Phone1()
myObj.feature1()
myObj.feature3()#give an error
myObj.feature2()#give an error