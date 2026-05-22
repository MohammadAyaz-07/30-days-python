import re

txt = '''Hello Ayyu 
how are you ayyu?'''
match = re.match("Hello", txt , re.I)
print(match)

span = match.span()
print(span)

start, end = span
print(start, end)

# we dont use the match() much so we use the search() most
# syntax: re.search(substring, string, re.I) re.I is case ignore flag, substring is 
# the pattern we are looking in the string, string is the string

match2 = re.search('you', txt, re.I)
print(match2)

# Now lets go for the findall() ; it returns all the matches as a list
match3 = re.findall('ayyu', txt, re.I)
print(match3)

# now without using the re.I to get the both the case ignore we use different methods

match4 = re.findall("Ayyu|ayyu", txt) # or '[Aa]yyu'
print(match4)

# Replacing a sub string
match_replaces = re.sub('Ayyu|ayyu', "Ayaz", txt)
print(match_replaces)

# Splitting Text 

print(re.split('\n', txt)) #splits the new line and returns in a list

# To declare a string variable we use ' or " or ''' but to declare RegEx variable we use r"
# the pattern only identifies the r' not others

