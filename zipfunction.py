names=['Rimdi','Tharaka','Sahan','Nadeesha','Sajith']
age=[20,21,22,23,24]
marks=[80,90,70,60,50]
details=tuple(zip(names,age,marks))  # Combines two lists into a list of tuples
print(details)  # Output: [('Rimdi', 20), ('Tharaka', 21), ('Sahan', 22), ('Nadeesha', 23), ('Sajith', 24)]

unzip=tuple(zip(*details))  # Unzips the list of tuples back into separate lists
print(unzip)  # Output: (('Rimdi', 'Tharaka', 'Sahan', 'Nadeesha', 'Sajith'), (20, 21, 22, 23, 24), (80, 90, 70, 60, 50))   
