import re
# Asabenah repo's 

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
# sub() is used to replace the substring with the new string, syntax: re.sub(pattern, new_string, string) 
match_replaces = re.sub('Ayyu|ayyu', "Ayaz", txt)
print(match_replaces)
# replacing % with space:

t = "I%am%Ayaz"
match_replaces2 = re.sub('%', ' ', t)
print(match_replaces2) # we can also use re.sub() to remove the substring by replacing it with empty string


# Splitting Text 

print(re.split('\n', txt)) #splits the new line and returns in a list

# Regex patterns:
# To declare a string variable we use ' or " or ''' but to declare RegEx variable we use r"
# the pattern only identifies the r' not others
pattern, new_string = r'\b\w+b\ayaz\f', "Ayaz" # this is a pattern to match the word 'ayaz' with word boundary and form feed
print(pattern)
print(new_string) #this is the new string we want to replace with the pattern

n = "I am Ayaz and I am learning regex"
# to replace the pattern with the new string we use re.sub() method
f = re.sub(pattern, new_string, n)
print(f) # this will replace the word 'ayaz' with 'Ayaz' in the string n if it matches the pattern

# Now lets see some of the regex patterns:
# \a is a word boundary, it matches the position where a word starts or ends
# []: it is used to match any one of the characters inside the brackets, for example [Aa] will match for A and a
# \w matches any word char (letters, digits, underscore)
# Lets make short notes of the regex patterns:
# \b: word boundary, it matches the position where a word starts or ends
# \w: word character (letters, digits, underscore)
# \d: digit
# \s: whitespace character (space, tab, newline)
# \A: start of the string
# \Z: end of the string eg: \AHello will match for Hello at the start of the string, \ZHello will match for Hello at the end of the string
# |: or operator, it matches either the pattern before or after the operator eg: Ayyu|ayyu will match for Ayyu or ayyu
# .: it matches any character except newline eg: a.b will match for a followed by any character followed by b, it will match for aab, acb, but not for ab
# ^ : it matches the start of the string eG: ^Hello will match for Hello at the start of the string 
# $ : it matches the end of the string eg: $Hello will match for Hello at the end of the string
# *: means zero or more occurrences of the preceding character eg: a* will match for '', a,...
# +: means one or more occurrences of the preceding character eg: a+ will match for a, aa, aaa ...
# ?: means zero or one occurrence of the preceding character eg: a? will match for '' and a
# {}: means exactly the specified number of occurrence of the preceding character eg: a{3} will match for aaa
# (): it is used to group the character eg: (ab)+ will match for ab, abab...

# Negation: [^a-z] will match for any character except a to z, [^0-9] will match for any character except digits

# Quantifiers: {m,n} means at least m and at most n occurrences of the preceding character eg: a{2,4} will match for aa, aaa, aaaa but not for a or aaaaa
txt = "I am Ayaz and I am learning regex today is 22-06-2026 and tommorow in 5 years will be 23-06-2031"
# to find all the years in the string we use \d{4}
years = re.findall(r'\d{4}', txt)
print(years) # this will return a list of all the years in the string txt

# Zero or one time(?):
txt2 = "email, E-mail, Email, eMail"
regx = r'[Ee]-?mail' # this will match for email, E-mail, EMAIL
matches = re.findall(regx, txt2)
print(matches) # this will return a list of all the matches in the string txt2 the -? means that the - is optional, it can be there or not 

# Zero or more times(*):
txt3 = "color, colour, Colour, Color"
regx2 = r'[Cc]olou?r' # this will match for color, colour, Colour, Color the u? means u is opt , it can be there or not
match2 = re.findall(regx2, txt3)
print(match2) # this will return a list of all the matches in the string txt3

# Period(.):
txt4 = "cat, cot, cut, cit"
regx3 = r'c.t' # this will match for cat, cot, cut, cit the . means any character except newline
match3 = re.findall(regx3, txt4)
print(match3) # this will return a list of all the matches in the string txt4
# here what does the new line mean? it means that the . will not match for newline char, it will match for any char except newline char, so if we have a string like "c\nt" the . will not match for \n but it will match for any other char

# Thats all for the regex patterns, we will see more patterns in the next days, but these are the basic patterns that we use most of the time in our regex operations.