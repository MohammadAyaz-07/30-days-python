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