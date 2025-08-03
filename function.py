def student(subject , marks):
    print("Subject = ",subject)
    print("Marks = ",marks)
student("Maths",98)  

#affecting of the by default arguments 
def student(subject="Physics" , marks=45):
    print("Subject = ",subject)
    print("Marks = ",marks)
student("Maths",98)  #output is still Maths,98

def student(subject="Physics" , marks=45):
    print("Subject = ",subject)
    print("Marks = ",marks)
student("Maths")  #so now it replaced by the default value since it doesn't give an value for the marks

#want to add more than one parameter values to an parameter you have to put a astric * at the beginnig of the argument
def student(subject , marks,*friends):
    print("Subject = ",subject)
    print("Marks = ",marks)
    print("Friends = ",friends)
student("Maths",98,"Ridmi","Tharaka") 

#to add dictionary like ridmi , 65 you have to put two astric marks 
def student(subject , marks,**friends):
    print("Subject = ",subject)
    print("Marks = ",marks)
    print("Friends = ",friends)
student("Maths",98,Ridmi=68,Tharaka=70) 