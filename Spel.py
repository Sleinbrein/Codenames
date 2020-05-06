import random


class Spel:
    bord = []
    wordlist = []

    def __init__(self):
        pass

    def getWordList(self):
        with open("words.txt") as file:
            woordendata = file.read()
        lines = woordendata.splitlines()

        for i in range(25):
            self.wordlist.append(lines[random.randrange(0, len(lines))])

        return self.wordlist

    def asignColor(self):
        kansgetal = random.randint(0, 1)
        if kansgetal == 0:
            firstColor = 'red'
            secondColor = 'blue'

        else:
            firstColor = 'blue'
            secondColor = 'red'

        self.getWordList()

        # geef het startende team 9 woorden in hun kleur
        for i in range(9):
            self.bord.append(
                [self.wordlist[i], firstColor]
            )

        # geef het andere team 8 woorden in hun kleur
        for i in range(8, 25):
            self.bord.append(
                [self.wordlist[i], secondColor]
            )

        return self.bord

    def everythingUnvisible(self):
        self.getWordList()
        self.asignColor()

        for tegel in self.bord:
            tegel.append(False)
            print(tegel)

