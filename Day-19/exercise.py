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