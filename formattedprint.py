name,age ,score = 'Ridmi',24,43.567

# #She is Ridmi She is 24 years old ,and her score is 43.567
# print('She is '+name +'. She is '+str(age) + 
#       ' years old , and her score is '+str(score)) 

print("She is %s. She is %d years old , and her score is %.2f " %(name,age,score))
print("She is {}. She is {} years old , and her score is {}" .format(name,age,score))
print(f"She is {name}. She is {age} years old , and her score is {score}")