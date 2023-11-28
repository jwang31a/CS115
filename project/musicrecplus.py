"""
when program launches:
 -check if txt file exists, create if it doesn't
 -read the file?
 -get user input for name and artists
 -sanitize data, turn artists into titlecase using title()
 -check if name exists in txt, if it does, skip preferences input, go to menu? (no duplicate users)
 -if it doesn't, create a new row and put user input into txt
 -order the usernames?
 -program should be a while loop that offers menu choices

username:artist1,artist2,artist3...
$ at end for private information

menu is:
Enter a letter to choose an option :
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit
"""

def enterPrefs():
    """
    takes in inputs
    at end, return to menu
    """
    artists = []
    gettingInputs = True
    while gettingInputs:
        newArtist = input("Enter an artist that you like ( Enter to finish ): ").title()
        if newArtist == "":
            gettingInputs = False
        else:
            artists += [newArtist]
    with open("musicrecplus.txt", "a") as musicFile:
        musicFile.writelines(artists)
    showMenu()

def showMenu():
    choice = input("""Enter a letter to choose an option :
    e - Enter preferences
    r - Get recommendations
    p - Show most popular artists
    h - How popular is the most popular
    m - Which user has the most likes
    q - Save and quit\n""")
    return choice

def main():
    enterPrefs()

main()