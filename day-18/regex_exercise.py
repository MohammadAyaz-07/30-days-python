# Today we are going to solve the exercise problems of this day
'''
Exercises: Level 1
1. What is the most frequent word in the following paragraph?
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20

'''

# lets solve the first problem:
from pydoc import text
import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# to find the most frequent word in the para we can use the re.findall() method to find all the words in the para and then use the counter to find the most freqency word
words = re.findall(r'\b\w+\b', paragraph) # this will find all the words in the para and return a list of words 
# here in re.findall(r'\b\w+\b', paragraph) the r' means raw string, \b means word boundary, \w means word char (letters, digits, underscore), + means one or more occurrences of the preceding char, so this pattern will match for any word in the para and return a list of all words
print(words) # this will print the list of words in the para
# lets find the frequency of each word manually:
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1
    # now we have the frequency of each word in the word_freq dict, we can sort the dict by value to find the most frequent word
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True) # This will sort the dict by value in descending order
print(sorted_word_freq[:5]) # this will print the sorted dict of word frequency
 # now we can see that the most frequent word is 'love' with a frequency of 6~

# Lets solve the second problem:
# to extract the numbers from the text we can use the re.findall() methodn \d+ will match for one or more digits, -? will match for optional negative sign
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
numbers = re.findall(r'-?\d+', text)
print(numbers) # this will print the list of numbers in the text
# now we can convert the list of numbers to integers and sort them to find the distance between the two furthest particles
int_numbers = [int(num) for num in numbers] # this will convert the list of numbers to integers
sorted_numbers = sorted(int_numbers) # this will sort the list of numbers
print(sorted_numbers) # this will print the sorted list of numbers
d = sorted_numbers[-1] - sorted_numbers[0] # this will find the distance between the two furthest particles
print(d)  


# Now Exercises: Level 2
'''
Write a pattern which identifies if a string is a valid python variable

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
'''


