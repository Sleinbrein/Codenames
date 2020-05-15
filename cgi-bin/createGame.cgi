#!/usr/bin/python3

import json
import cgi
import game


'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''global gamecode = crea
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'toevoegen':
    verzenden['gamecode'] = game.getGamecode()
    verzenden['board'] = game.createGame()
    verzenden['current_color'] = 'red'
    verzenden['winner'] = None  

'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
