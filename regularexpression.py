import re
#\d(0-9),\w((a-zA-Z0-9_)+),\s( ),\S(not\space),\W(not\word)

str = 'Ridmi Wickramasinghe 1234'
y=re.findall('\d',str)  # Finds all digits in the string
print(y)  # Output: ['1', '2', '3', '4']

y=re.findall('\w',str)  # Finds all word characters in the string
print(y)  # Output: ['R', 'i', 'd', 'm', 'i', 'W', 'i', 'c', 'k', 'r', 'a', 'm', 'a', 's', 'i', 'n', 'g', 'h', 'e', '1', '2', '3', '4']

y=re.findall('\s',str)  # Finds all whitespace characters in the string
print(y)  # Output: [' ', ' ']

y=re.findall('\S',str)  # Finds all non-whitespace characters in the string
print(y)  # Output: ['R', 'i', 'd', 'm', 'i', 'W', 'i', 'c', 'k', 'r', 'a', 'm', 'a', 's', 'i', 'n', 'g', 'h', 'e', '1', '2', '3', '4']

y=re.findall('\w\w\w\w\w\w',str)  # Finds all non-word characters in the string