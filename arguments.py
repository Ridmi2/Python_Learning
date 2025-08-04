#positional arguments
def student_infor(name,age):
    print(f"My name is {name}.My age is {age}")
student_infor("Ridmi",25)    
    
#keyword arguments
def student_infor(name,age):
    print(f"My name is {name}.My age is {age}")
student_infor(age=25,name="Ridmi") 

#both keyword and positional using put positional one first otherwise it give an error.then use all otthers by keyword
def student_infor(name,age):
    print(f"My name is {name}.My age is {age}")
student_infor("Ridmi",age=25) 

#default arguments 
def student_infor(name,age=25):
    print(f"My name is {name}.My age is {age}")
student_infor("Ridmi") 

def student_infor(name,age):
    print(f"My name is {name}.My age is {age}")
student_infor("Ridmi",age=17) 

#variable length arguments
def total_marks(*marks):
    print(marks)
total_marks(30,67,56)    

def total_marks(*marks):
    total =0
    for i in marks:
        total+=i
    print("Total marks : ",total)
total_marks(30,67,56)    

#variable length with keyword arguments -we have to use two astricts as it get keyworded arguments
def total_marks(**marks):
    for sub,mark in marks.items():
        print(sub,mark)
total_marks(maths=56,science=78,english=90)        
