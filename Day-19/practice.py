f = open("file.txt", "w")
f.write("I am learning Python today's date is 3 June 2026")
print(f)
f.close()

f = open("file.txt", "a")
txt = f.write("\nThis is 3rd line text")

# To check whether a file is not empty:
with open("file.txt", "a+") as file:
    file.seek(0)
    if file.read(1):
        file.write("\n")
    file.write("New line appended")

f = open("file.txt")
txt2 = f.read(10)
print(txt2)
f.close()

f = open('file.txt')
txt3 = f.readlines()
print(txt3) # Readlines returns all the lines in a list

with open("file.txt") as f:
    lines = f.read().splitlines()
    print(lines)

with open('file.txt', "a") as f:
    f.write("This will the last line of the file")

with open("file2.txt", "w") as f:
    f.write("this text will be written in a newly created file")

# Deleting files:
import os
os.remove("file2.txt")
# to check if file doesnt exist:

if os.path.exists("file3.txt"):
    os.remove("file3.txt")
else:
    print("File doesnt exitst!")

# File types :
# dictionary
ayaz_dict = {
    "name" : "Ayaz",
    "country" : "India",
    "age" : 18,
    "skills" : ["Python"]
}

# json : A string form of a dict

# Changing JSON to Dict (we use loads method)
ayaz_json = '''{
    "name" : "Ayaz",
    "country" : "India",
    "age" : 18,
    "skills" : ["Python"]
}'''
import json
ayaz_json = '''{
    "name" : "Ayaz",
    "country" : "India",
    "age" : 18,
    "skills" : ["Python"]
}'''

ayazz_dict = json.loads(ayaz_json)
print(type(ayazz_dict))
print(ayazz_dict)
print(ayazz_dict["name"])

# Changing Dict to JSON (we use dumps method)
ayazz_json = json.dumps(ayaz_json, indent=4) # indent could be 2,4,6,8.It beautifies the json
print(type(ayazz_json))
print(ayazz_json)

with open("json_example.json", "w", encoding='utf-8') as f:
    json.dump(ayazz_json, f, ensure_ascii=False, indent=4)


# File w csv extension

# ex for csv is:
"name","country","age","skills"
"Ayaz","India",18,["Python"]

import csv
with open("csv_example.csv", "r") as f:
    csv_reader = csv.reader(f, delimiter=',') # we use , reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are: {", ".join(row)}")
            line_count += 1
        else:
            print(f"\t{row[0]} is a Student. He lives in {row[1]}.")
            line_count += 1
    print(f"Number of lines = {line_count}")