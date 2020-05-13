#!/usr/bin/python3

import json
import cgi


'''
PYTHON FUNCTIES
'''

def printSomething():
    return "Hello World"


'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

clickdata = json.loads(cgi.FieldStorage().getvalue('clickdata'))


'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if clickdata['actie'] == 'clickontile':
    verzenden['lijst'] = printSomething()



'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
