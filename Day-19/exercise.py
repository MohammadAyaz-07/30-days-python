# Exercise: Level 1
'''
1.Write a function which count number of lines and number of words in a text. All the files are in the data the folder:

i. Read obama_speech.txt file and count number of lines and words
ii. Read michelle_obama_speech.txt file and count number of lines and words
iii. Read donald_speech.txt file and count number of lines and words
iv. Read melina_trump_speech.txt file and count number of lines and words
'''
import os
if os.path.exists("obama.txt"):
    print("Files exists")
else:
    print("Doesnt exists")

def no_of_line_and_words(file):
    with open(file) as f:
        txt = f.read()
        print(f"Number of words: {len(txt.split())}")
        f.seek(0)
        print(f"Number of lines: {len(f.readlines())}")

no_of_line_and_words("obama.txt")
no_of_line_and_words("michelle_obama_speech.txt")
no_of_line_and_words("donald_speech.txt")
no_of_line_and_words("melina_trump_speech.txt")

'''
2.Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]
'''
import json

def most_spoken_lang(filename,n):
    with open(filename, encoding="utf-8") as f:
        countries = json.load(f)
        lang_count = {}
        for country in countries:
            for language in country["languages"]:
                lang_count[language] = lang_count.get(language , 0) + 1
        s = lang_count.items()
        sorted_lang = sorted(s, key=lambda x: x[1], reverse=True)
        return sorted_lang[:n]

print(most_spoken_lang(filename="countries_data.json", n=5))

'''
3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

# Your output should look like this
print(most_populated_countries(filename='./data/countries_data.json', 10))

[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
]

# Your output should look like this

print(most_populated_countries(filename='./data/countries_data.json', 3))
[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000}
]
'''

def most_populated_countries(filename, n):
    with open(filename, encoding="utf-8") as f:
        countries = json.load(f)
        population_list = []
        for country in countries:
            c = country["name"]
            p = country["population"]
            ed = {"country": c, "population": p}
            #now we have to take only the top 10 countries with the highest population
            population_list.append(ed)
        sorted_ed = sorted(population_list, key=lambda x: x["population"], reverse=True)
        return sorted_ed[:n]
print(most_populated_countries(filename="countries_data.json", n=10))

'''
Exercises: Level 2
1. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
'''
import re
with open("email_exchange_big.txt") as f:
    text = f.read()
    pattern = re.findall(r"\b\w+[@]\w+[.]\w+\b", text, re.I )
print(pattern)

'''
2. Find the most common words in the English language. Call the name of your function find_most_common_words,
 it will take two parameters - a string or a file and a positive integer, indicating the number of words. 
 Your function will return an array of tuples in descending order. Check the output

    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
'''

def find_most_common_words(filename, n):
    with open(filename) as f:
        text = f.read()
        txt = re.findall("\w+", text, re.I)
        count = {}
        for w in txt:
            count[w] = count.get(w, 0) + 1
        c = count.items()
        cc = sorted(c, key=lambda x: x[1], reverse=True)
        r = []
        for x in cc:
            xx = (x[1], x[0])
            r.append(xx)
        return r[:n]
print(find_most_common_words("sample.txt", 5))

