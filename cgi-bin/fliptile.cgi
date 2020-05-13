#!/usr/bin/python3

import json
import cgi

'''
PYTHON FUNCTIES
'''

def fliptile(woord):
    return woord
    # try to open the datafile with the input gamecode if it exsists
    # filedirectory = "data/" + data['gameID'] + ".json"
    # filedirectory = "data/EKF7QMDB.json"

    # with open(filedirectory) as json_file:
    #     gamedata = json.load(json_file)
    #     return gamedata

    # return "Ik draai de tegel om server-sided"

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
    verzenden['lijst'] = fliptile(data['woord'])


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
