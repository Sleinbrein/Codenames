import json
import cgi
import random
import string

# CREATE GAME
def createGameCode(length=8):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return code

gamecode = createGameCode()
def getGamecode():
    return gamecode

def createGame():
    bord = []
    wordlist = []
    with open("words.txt") as file:
        woordendata = file.read()
    lines = woordendata.splitlines()

    while len(wordlist) != 25:
        if lines[random.randrange(0, len(lines))] not in wordlist:
            wordlist.append(lines[random.randrange(0, len(lines))])



    kansgetal = random.randint(0, 1)
    if kansgetal == 0:
        createGame.currentTeam = 'red'
        createGame.resterende_tegels_red = 9
        createGame.resterende_tegels_blue = 8
        firstTeam = 'red'
        secondTeam = 'blue'
    else:
        createGame.currentTeam = 'blue'
        createGame.resterende_tegels_red = 8
        createGame.resterende_tegels_blue = 9
        firstTeam = 'blue'
        secondTeam = 'red'


    # geef het startende team 9 woorden in hun kleur
    for i in range(9):
        bord.append(
            [wordlist[i], firstTeam]
        )

    # geef het andere team 8 woorden in hun kleur
    for i in range(9, 17):
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

    # shuffle de tegels
    random.shuffle(bord)


    # save data the JSON file
    verzenden = {
        "gamecode": gamecode,
        "board": bord,
        "current_color": createGame.currentTeam,
        "resterende_tegels_red": createGame.resterende_tegels_red,
        "resterende_tegels_blue": createGame.resterende_tegels_blue,
        "winner": None
    }

    # write gamedata to GAMECODE.json file
    with open("data/" + gamecode + ".json", 'w') as fileoutput:
        json.dump(verzenden, fileoutput)

    return bord










# FLIP TILE

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



    # update data to the same file
    with open(filedirectory, 'w') as f:
        json.dump(gamedata, f)

    return gamedata['board']








# SPYMASTER COLORS

def getSelectedColors(gameID):
    # open the datafile with the input gamecode
    gameID = gameID.replace("Share this code: ", "")
    filedirectory = "data/" + gameID + ".json"

    with open(filedirectory) as json_file:
        gamedata = json.load(json_file)

        # array van booleans
        chosenWords = []
        for word in gamedata['board']:
            chosenWords.append(word[2])

        return chosenWords