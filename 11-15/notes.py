"""
default function called input
input returns string, so typecast if want other type

can also open files from python using open(filename, mode)
mode is read/write
"""

def greeting():
    name = input("what your name? ")
    print("Nice to meet you, ", name)

# greeting()

"""
write mode clears file and replaces with new inputs (like overwrite)
append adds to file
closing is recommended for security purposes
also good idea to use delimiter (like a comma to separate string) in order to make split useful

split function to split string
strip function to remove leading and trailing spaces
join function to convert elements of iterable into string
capitalizze converts first character to uppercase
 -different from upper() or lower() which acts on whole string
"""
def write_file(filename, string):
    myfile = open(filename, "w")
    myfile.write(string)
    myfile.close()

filename = "newfile.txt"
write_file(filename, "name1, name2, name3, name4")

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    names = content.split(", ")
    for name in names:
        print(name)

read_file("newfile.txt")

"""
can also use with open() which automatically closes file
readlines stores in list
read reads line by line


"""

def readPrefs(filename):
    stuff = open(filename, "r")
    content = stuff.read()
    info = content.split("\n")
    print(info)
    preferences = {}
    for str in info:
        [username, artists] = str.strip().split(":")
        artists = artists.split(",")
        preferences[username] = artists
    print(preferences)

readPrefs("recsys.txt")

"""
pseudocode yay
not standardized, but much easier to read no matter what language a person knows
"""