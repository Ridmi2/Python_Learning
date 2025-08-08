import random
x=random.random()
print(x)  # Generates a random float between 0.0 and 1.0

import random
x=random.random()*10  # Generates a random float between 0.0 and 10.0
print(x) 

import random
x=random.uniform(5,10)  # Generates a random float between 5.0 and 10.0
print(x) 

import random
x=random.randint(4,12)
print(x)

name=['Ridmi', 'Wickramasinghe', 'Kavindu', 'Nadeesha']
winner = random.choice(name)  # Randomly selects an element from the list
print(winner)

name=['Ridmi', 'Wickramasinghe', 'Kavindu', 'Nadeesha']
winner = random.choices(name,k=2)  # Randomly selects an element from the list
print(winner)

numbers=list(range(1, 10))
print(numbers)
random.shuffle(numbers)  # Shuffles the list in place
print(numbers)