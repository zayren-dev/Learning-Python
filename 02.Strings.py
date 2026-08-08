#  in order to create multi-line strings , use double triple quotes (""" """) 
# or single triple quotes (''' ''')
string = '''I love learning Python, because it is easy to learn
and understand. It is a very powerful programming language. and also 
easy to read and write. It is used in many areas of software development,
including web development, data science, artificial intelligence, and more.'''
print(string)
#concatenaton of strings
first_name = 'Zayn'
last_name = 'ul Arifeen'
full_name = first_name + ' ' + last_name
print(full_name)
# using len function to get the length of a string
string_length = len(full_name)
print("Length of the string is:", string_length)
# Old style formatting using % operator
first_name = 'Zayn'
last_name = 'ul Arifeen'
full_name = ' %s %s ' % (first_name, last_name)
print(full_name)
# New style formatting using format() method

first_name = 'zayn'
last_name = 'ul Arifeen'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# f-strings (formatted string literals) are a more concise and readable way to format strings 
# in Python. They were introduced in Python 3.6 and allow you to embed
# expressions inside string literals using curly braces {} 
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

#string reversing
text = "Hello, World!"
print(text[::-1]) # Output: !dlroW ,olleH

# string methods
text = "my name is zayn ul arifeen"
print(text.capitalize()) # Output: My name is zayn ul arifeen
print(text.upper()) # Output: MY NAME IS ZAYN UL ARIFEEN
print(text.endswith('feen')) # Output: True
print(text.startswith('my')) # Output: True
print(text.find('zayn')) # Output: 11
print(text.count('a')) # Output: 2
print(text.replace('zayn ul arifeen', 'John Roberts')) # Output: my name is John Roberts

text2= 'thirty\tdays\tof\tpython'
print(text2.expandtabs())   # 'thirty  days    of      python'
print(text2.expandtabs(10)) # 'thirty    days      of        python'

