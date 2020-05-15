#!/usr/bin/python3

import json
import cgi
import os.path

'''
PYTHON FUNCTIES
'''


def refreshgame(gameID):
    # try to open the datafile with the input gamecode if it exsists
    gameID = gameID.replace("Share this code: ", "")
    filedirectory = "data/" + gameID + ".json"

    with open(filedirectory) as json_file:
        gamedata = json.load(json_file)

        return gamedata


'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'refresh':
   verzenden['updateddata'] = refreshgame(data['gameID'])


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
