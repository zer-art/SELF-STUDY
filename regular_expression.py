import re

# meta characterer in python 
''' 
r is used for raw string 
[] used to define classes [A-Z] , [a-z] ,[a,s,c]
^ matches the begining
'''
pattern = r'[C]omputer'
text = '''
A laptop computer or notebook Computer, also known as a laptop or notebook, is a small, portable personal computer (PC). Laptops typically have a clamshell form factor with a flat-panel screen on the inside of the upper lid and an alphanumeric keyboard and pointing device on the inside of the lower lid.[1][2] Most of the computer's internal hardware is in the lower part, under the keyboard, although many modern laptops have a built-in webcam at the top of the screen, and some even feature a touchscreen display. In most cases, unlike tablet computers which run on mobile operating systems, laptops tend to run on desktop operating systems, which were originally developed for desktop computers.
'''

# find only first occurance 
match = re.search(pattern , text)
if match : 
    print( "match found")
else : 
    print( "match not found")

# find all occurance    
matchs = re.finditer(pattern , text)
for match in matchs : 
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])

print(type(match.span()))


