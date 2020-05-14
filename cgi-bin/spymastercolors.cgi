#!/usr/bin/python3

import json
import cgi

'''
PYTHON FUNCTIES
'''

def getSelectedColors(gameID):
    # open the datafile with the input gamecode
    gameID = gameID.replace("Share this code: ", "")
    filedirectory = "data/" + gameID + ".json"

    with open(filedirectory) as json_file:
        gamedata = json.load(json_file)

        # array van booleans
        chosenWords = []
        for word in gamedata['board']:
            chosenWords.append(word[2])

        return chosenWords



'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'getselectedcolors':
    verzenden['selectedColors'] = getSelectedColors(data['gameID'])


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
