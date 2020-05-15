#!/usr/bin/python3

import json
import cgi



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
