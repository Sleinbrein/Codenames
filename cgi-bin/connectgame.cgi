#!/usr/bin/python3

import json
import cgi
import os.path

'''
PYTHON FUNCTIES
'''


def printSomething():
    return "Hello World"


'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'connectgame':
    # try to open the datafile with the input gamecode if it exsists
    filedirectory = "data/" + data['gameID'] + ".json"
    if os.path.exists(filedirectory):
        with open("data/" + data['gameID'] + ".json") as json_file:
            jsondata = json.load(json_file)
            verzenden['gameinfo'] = jsondata['board']
    else:
        verzenden['gameinfo'] = "Invalid Gamecode!"

    verzenden['lijst'] = printSomething()
    verzenden['testje'] = data['gameID']

'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
