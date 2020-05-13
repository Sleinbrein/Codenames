#!/usr/bin/python3

import json
import cgi

'''
PYTHON FUNCTIES
'''

def fliptile(woord, gameID):
    # open the datafile with the input gamecode
    gameID = gameID.replace("Share this code: ", "")
    filedirectory = "data/" + gameID + ".json"

    with open(filedirectory) as json_file:
        gamedata = json.load(json_file)

        for tile in gamedata['board']:
            if tile[0] == woord:
                # flip the tile if we can
                if tile[2] == False:
                    tile[2] = True


    # update data to the same file
    with open(filedirectory, 'w') as f:
        json.dump(gamedata, f)

    return gamedata['board']

'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'fliptile':
    verzenden['gamecode'] = data['gameID']
    verzenden['lijst'] = fliptile(data['woord'], data['gameID'])


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
