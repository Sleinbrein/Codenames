#!/usr/bin/python3

import json
import cgi
import game

'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'getselectedcolors':
    verzenden['selectedColors'] = game.getSelectedColors(data['gameID'])


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
