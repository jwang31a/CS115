"""
given a word with repeat letters, figure out if list of chars can form that word
"""
def repeatFilter(chars, word, usedChars):
    if chars == []:
        return True
    elif word == "":
        return True
    else:
        # print("==============" + str(chars) + " === " + word)
        if word[0] in chars:
            i = findIndex(word[0], chars)
            usedChars += chars[i]
            return repeatFilter(chars[:i] + chars[i + 1:], word[1:], usedChars)
        else:
            return False

def findIndex(char, list):
    if list == []:
        return float("inf")
    elif char == list[0]:
        return 0
    else:
        return 1 + findIndex(char, list[1:])

chars = ["a", "p", "p", "l", "e"]
# print(findIndex("e", chars))
# print(findIndex("j", chars))

print(repeatFilter(chars, "apple", []))
print(repeatFilter(chars, "aple", []))
print(repeatFilter(chars, "applle", []))

# print(float("inf") == float("inf"))