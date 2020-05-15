
import random
import string
import json


class Spel:
    # representatie van het spelbord like [["Android", 'red', false], ... ]
    bord = []

    # 25 random gekozen woorden
    wordlist = []

    # de code nodig voor een spel te kunnen joinen
    gamecode = ''

    # bijhouden welk team (ROOD | BLAUW) er momenteel aan de beurt is
    currentTeam = ''

    #bijhouden wie de winnaar is
    winner = ''

    def __init__(self):
        self.createGameCode(8)
        print(f"Het spel wordt gestart met code {self.gamecode}")

    def createGameCode(self, length=8):
        self.gamecode = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def getWordList(self):
        with open("words.txt") as file:
            woordendata = file.read()
        lines = woordendata.splitlines()

        for _ in range(25):
            self.wordlist.append(lines[random.randrange(0, len(lines))])

        return self.wordlist


    def asignColor(self):
        kansgetal = random.randint(0, 1)
        if kansgetal == 0:
            self.currentTeam = 'red'
            firstTeam = 'red'
            secondTeam = 'blue'
        else:
            self.currentTeam = 'blue'
            firstTeam = 'blue'
            secondTeam = 'red'

        # geef het startende team 9 woorden in hun kleur
        for i in range(9):
            self.bord.append(
                [self.wordlist[i], firstTeam]
            )

        # geef het andere team 8 woorden in hun kleur
        for i in range(9, 17):
            self.bord.append(
                [self.wordlist[i], secondTeam]
            )

        # 7 neutrale tegels
        for i in range(17,24):
            self.bord.append(
                [self.wordlist[i], "#8B9FB3"]
            )

        # laatste tegel is de spymaster
        self.bord.append([self.wordlist[24], "#2d3436"])



    def everythingUnvisible(self):
        for tegel in self.bord:
            tegel.append(False)
        return self.bord

    def switchTeam(self):
        if self.currentTeam == 'red':
            self.currentTeam = 'blue'
        else:
            self.currentTeam = 'red'

    def playTurn(self):
        pass


    def toJson(self):
        verzenden = {
            "code": self.gamecode,
            "board": self.bord,
            "current_color": self.currentTeam,
            "winner": None
        }

        # write gamedata to GAMECODE.json file
        with open("data/" + self.gamecode + ".json", 'w') as fileoutput:
            json.dump(verzenden, fileoutput)


    def getJson(self):
        with open('data/' + self.gamecode + '.json') as file:
            data = json.load(file)

            #update variables
            self.bord = data['board']
            self.winner = data['winner']
            self.currentTeam = data['current_color']

            print(f"Het bord: {self.bord}\nWie is er aan de beurt: {self.currentTeam}\nWie heeft er gewonnen: {self.winner}")


spel = Spel()
spel.getWordList()
spel.asignColor()
spel.everythingUnvisible()
print(spel.toJson())
