#!/usr/bin/python3

import json
import cgi
import random
import string

'''
PYTHON FUNCTIES
'''

def createGameCode(length=8):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return code

gamecode = createGameCode()

def createGame():
    bord = []
    wordlist = []
    with open("words.txt") as file:
        woordendata = file.read()
    lines = woordendata.splitlines()

    for _ in range(25):
        wordlist.append(lines[random.randrange(0, len(lines))])


    kansgetal = random.randint(0, 1)
    if kansgetal == 0:
        createGame.currentTeam = 'red'
        firstTeam = 'red'
        secondTeam = 'blue'
    else:
        createGame.currentTeam = 'blue'
        firstTeam = 'blue'
        secondTeam = 'red'


    # geef het startende team 9 woorden in hun kleur
    for i in range(9):
        createGame.resterende_tegels_firstteam = 9
        bord.append(
            [wordlist[i], firstTeam]
        )

    # geef het andere team 8 woorden in hun kleur
    for i in range(9, 17):
        createGame.resterende_tegels_lastteam = 8
        bord.append(
            [wordlist[i], secondTeam]
        )

    # 7 neutrale tegels
    for i in range(17, 24):
        bord.append(
            [wordlist[i], "#8B9FB3"]
        )

    # laatste tegel is de spymaster
    bord.append([wordlist[24], "#2d3436"])


    # draai elke tegel om
    for tegel in bord:
        tegel.append(False)


    # save data the JSON file
    verzenden = {
        "gamecode": gamecode,
        "board": bord,
        "current_color": createGame.currentTeam,
        "winner": None
    }

    # write gamedata to GAMECODE.json file
    with open("data/" + gamecode + ".json", 'w') as fileoutput:
        json.dump(verzenden, fileoutput)

    return bord



'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'toevoegen':
    verzenden['gamecode'] = gamecode
    verzenden['board'] = createGame()
    verzenden['current_color'] = createGame.currentTeam
    verzenden['winner'] = None

'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
