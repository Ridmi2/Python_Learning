class Phone:
    def say(self):
        print("Hello")
phone1=Phone()        
phone1.say()     

#if you give an argument rather than default self , you have to assign a value for that in method calling
class Phone:
    def say(self,name):
        print("Hello " + name)
phone1=Phone()        
phone1.say("Ridmi") 

phone2 =Phone()
phone2.say("John")

#calling for attributes
class Phone:
    def say(self,name):
        self.x=name
        print("Hello "+name)
phone1=Phone()        
phone1.say("Ridmi") 
print(phone1.x)
#can also chNGE THE VALUE OF ATTRIBUTE
phone1.x="Tharaka"
print(phone1.x)