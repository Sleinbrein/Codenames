import random

def getWordList():
    wordlist = []
    with open("words.txt") as file:
        woordendata = file.read()
    lines = woordendata.splitlines()

    for i in range(25):
        wordlist.append(lines[random.randrange(0, len(lines))])

    return wordlist