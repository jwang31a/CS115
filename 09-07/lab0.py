############################################################
# Name: Jun Hong Wang
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 1
#  
############################################################

def same(word):
    # return(word[0].lower() == word[-1].lower())
    return(word[0].lower() == word[len(word) - 1].lower())

def consecutiveSum(x, y):
    return(((x + y) / 2) * (y - x - 1))

# def main():
#     print(same("bobby"))
#     print(same("ResearcheR"))
#     print(same("stevenS"))

# main()