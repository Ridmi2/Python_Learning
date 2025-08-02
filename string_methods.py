name = 'Python Programming'
print(name)
# convert to uppercase 
print(name.upper())
#convert to lowercase
print(name.lower())
#convert every words'first letter only into capital 
print(name.title())
#only first lettor of the word se is capital
print(name.capitalize())
#find
print(name.find('g'))
print(name.find('Pro'))
print(name.find('P'))

print(name.find('d'))#give a atring that is not in the string will give an -1


print(name.find('P',1,8))#other P in the string
print(name.find('P',1,7))
#find in right side
print(name.rfind('P'))#2 nd P on programming is at 7th index


#index
#give a string that not in the string will return an error
#print(name.index('d'))


#alignment

print(name.ljust(20,"-"))
print(name.center(20,"-"))
print(name.rjust(20,"-"))

#remove spaces
name1 = "     Ridmi  "
print(name1.strip())#remove spaces
print(name1)

print(name1.lstrip())#remove  left sidespaces
print(name1.rstrip())#remove  right side spaces

name2 = "----Tharaka---"
print(name2.strip('-'))#remove  spaces
print(name2)

print(name2.lstrip('-'))#remove  left sidespaces
print(name2.rstrip('-'))