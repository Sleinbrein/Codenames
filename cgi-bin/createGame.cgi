#!/usr/bin/python3

import json
import cgi
import random

'''
PYTHON FUNCTIES
'''

def printSomething():
    # getallen = []
    # for i in range(10):
    #     getallen.append(i)
    # return getallen

    wordlist = []
    with open("words.txt") as file:
         woordendata = file.read()
    lines = woordendata.splitlines()

    for _ in range(25):
        wordlist.append(lines[random.randrange(0, len(lines))])
    return wordlist



'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))


'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'toevoegen':
    verzenden['woorden'] = printSomething()


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
