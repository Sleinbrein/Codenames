#!/usr/bin/python3

import json
import cgi

'''
PYTHON FUNCTIES
'''


'''Refresh de tiles wanneer deze methode wordt aangeroepen zodat alle spelers dezelfde informatie zien.'''
# def refreshgame(gameID):
#     # try to open the datafile with the input gamecode if it exsists
#     gameID = gameID.replace("Share this code: ", "")
#     filedirectory = "data/" + gameID + ".json"

#     with open(filedirectory) as json_file:
#         gamedata = json.load(json_file)

#         return gamedata


'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'refresh':
    # try to open the datafile with the input gamecode if it exsists
    filedirectory = "data/" + data['gameID'] + ".json"

    with open("data/" + data['gameID'] + ".json") as json_file:
        jsondata = json.load(json_file)
        verzenden['gameinfo'] = jsondata['board']
   
    # verzenden['lijst'] = refreshgame()
    # verzenden['testje'] = data['gameID']

'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
