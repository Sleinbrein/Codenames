#!/usr/bin/python3

import json
import cgi
import random

'''
PYTHON FUNCTIES
'''

def createGame():
    
    wordlist = []
    with open("words.txt") as file:
         woordendata = file.read()
    lines = woordendata.splitlines()

    for _ in range(25):
        wordlist.append(lines[random.randrange(0, len(lines))])

    # save data the JSON file
    verzenden = {
        "board": wordlist,
        "winner": None
    }

    # write gamedata to GAMECODE.json file
    with open("data/" + "AVCDEFGH" + ".json", 'w') as fileoutput:
        json.dump(verzenden, fileoutput)
    
    return wordlist


'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))


'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'toevoegen':
    verzenden['woorden'] = createGame()


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
