#!/usr/bin/python3

import json
import cgi

'''
PYTHON FUNCTIES
'''

def switchTeam(gameID):
    # open the datafile with the input gamecode
    gameID = gameID.replace("Share this code: ", "")
    filedirectory = "data/" + gameID + ".json"


    with open(filedirectory) as json_file:
        gamedata = json.load(json_file)


        if gamedata['current_color'] == 'red':
            
            gamedata['current_color'] = 'blue'
        else:
            gamedata['current_color'] = 'red'



     # write gamedata to GAMECODE.json file
    with open("data/" + gameID + ".json", 'w') as fileoutput:
        json.dump(gamedata, fileoutput)



'''
LEES DATA VERSTUURD DOOR JAVASCRIPT IN
'''

data = json.loads(cgi.FieldStorage().getvalue('data'))

'''
BEREKEN TE VERZENDEN DATA
'''

verzenden = dict()

if data['actie'] == 'endturn':
    verzenden['updateddata'] = switchTeam(data['gameID'])


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
