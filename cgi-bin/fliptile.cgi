#!/usr/bin/python3

import json
import cgi

'''
PYTHON FUNCTIES
'''

def fliptile(woord, gameID):
    # open the datafile with the input gamecode
    gameID = gameID.replace("Share this code: ", "")
    filedirectory = "data/" + gameID + ".json"


    with open(filedirectory) as json_file:
        gamedata = json.load(json_file)

        for tile in gamedata['board']:
            if tile[0] == woord:
                print(tile[0])
                # flip the tile if we can
                if tile[2] == False:
                    tile[2] = True

                    if gamedata['current_color'] == "red":
                        if tile[1] == 'red':
                            gamedata['resterende_tegels_red'] -= 1
                        elif tile[1] == 'blue':
                            # switch team
                            gamedata['current_color'] = 'blue'
                            gamedata['resterende_tegels_blue'] -= 1
                        elif tile[1] == '#8B9FB3': # neutraal
                            #switch team
                            gamedata['current_color'] = 'blue'
                        elif tile[1] == '#2d3436': # sluipmoordenaar
                            gamedata['winner'] = 'blue'
                    
                    elif gamedata['current_color'] == "blue":
                        if tile[1] == 'blue':
                            gamedata['resterende_tegels_blue'] -= 1
                        elif tile[1] == 'red':
                            # switch team
                            gamedata['current_color'] = 'red'
                            gamedata['resterende_tegels_red'] -= 1
                        elif tile[1] == '#8B9FB3': #neutraal
                            # switch team
                            gamedata['current_color'] = 'red'
                        elif tile[1] == '#2d3436': # sluipmoordenaar
                            gamedata['winner'] = 'red'



                            


    #     print(gamedata['resterende_tegels_red'])

    # return gamedata



    # update data to the same file
    with open(filedirectory, 'w') as f:
        json.dump(gamedata, f)

    return gamedata['board']

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
    verzenden['lijst'] = fliptile(data['woord'], data['gameID'])


'''
STUUR CGI ANTWOORD TERUG
'''

print("Content-Type: application/json")
print()

print(json.dumps(verzenden))
