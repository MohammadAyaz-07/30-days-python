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

