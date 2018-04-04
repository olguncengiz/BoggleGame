import random

class Board(object):
    def __init__(self):
        self.dice = [[u'\u0044', u'\u004C', u'\u0052', u'\u0059', u'\u0045', u'\u0059'],
                    [u'\u0054', u'\u0053', u'\u0054', u'\u0041', u'\u0059', u'\u0130'],
                    [u'\u0048', u'\u004C', u'\u004E', u'\u0052', u'\u0041', u'\u005A'],
                    [u'\u004B', u'\u0047', u'\u0055', u'\u0130', u'\u00DC', u'\u004B'],
                    [u'\u0053', u'\u0050', u'\u004B', u'\u0046', u'\u0041', u'\u0046'],
                    [u'\u015E', u'\u0045', u'\u0059', u'\u004C', u'\u0044', u'\u0052'],
                    [u'\u004F', u'\u004B', u'\u0130', u'\u004D', u'\u0043', u'\u004D'],
                    [u'\u00D6', u'\u004A', u'\u0130', u'\u0042', u'\u004F', u'\u0041'],
                    [u'\u0050', u'\u0130', u'\u0056', u'\u0041', u'\u0053', u'\u004F'],
                    [u'\u0049', u'\u015E', u'\u015E', u'\u0054', u'\u0045', u'\u004F'],
                    [u'\u0045', u'\u004E', u'\u0130', u'\u0045', u'\u0053', u'\u0055'],
                    [u'\u0048', u'\u0130', u'\u0055', u'\u005A', u'\u0055', u'\u004D'],
                    [u'\u0130', u'\u004D', u'\u00C7', u'\u004D', u'\u0044', u'\u004B'],
                    [u'\u0041', u'\u004E', u'\u0047', u'\u0045', u'\u004D', u'\u004E'],
                    [u'\u00C7', u'\u00DC', u'\u0042', u'\u004F', u'\u0041', u'\u011E'],
                    [u'\u00D6', u'\u004C', u'\u0042', u'\u0049', u'\u0044', u'\u0041']]
        self.size = 4
        self.letters = list()

    def shuffle(self):
        checkList = []
        for i in range(self.size):
            self.letters.append(list())
            for j in range(self.size):                
                found = False
                while not found:
                    row = random.randrange(len(self.dice))
                    if row not in checkList:
                        self.letters[i].append(self.dice[row][random.randrange(len(self.dice[0]))])
                        checkList.append(row)
                        found = True

        return {"letters": self.letters}

    def wordExists(self, word, path=None):
        if len(word) == 0 and len(path) == 0:
            return False
        elif len(word) == 0 and len(path) != 0:
            return True
        elif path == None:
            path = list()
            letter = word[0]
            for i in range(self.size):
                for j in range(self.size):
                    if self.letters[i][j] == letter:
                        path.append((i, j))
                        if self.wordExists(word[1:], path):
                            return True
                        else:
                            path.pop()
            return False
        elif path != None:
            letter = word[0]
            coordinates = path[-1]
            newCoordinates = self.getNeighborCells(coordinates, path)
            for i in range(len(newCoordinates)):
                newCell = newCoordinates[i]
                x = newCell[0]
                y = newCell[1]
                if self.lettersMatch(self.letters[x][y], letter):
                    path.append((x, y))
                    if self.wordExists(word[1:], path):
                        return True
                    else:
                        path.pop()
            return False

    def getNeighborCells(self, lastTuple, path):
        i = lastTuple[0]
        j = lastTuple[1]
        newCoordinates = list()
        for x in range(i - 1, i + 2, 1):
            for y in range(j - 1, j + 2, 1):
                if x == i and y == j:
                    pass
                elif (x, y) in path:
                    pass
                else:
                    if x < 0 or x > 3 or y < 0 or y > 3:
                        pass
                    else:
                        newCoordinates.append((x, y))
        return newCoordinates

    def printBoard(self):
        prnt = ""
        for i in range(self.size):
            line = u''
            for j in range(self.size):
                line = line + ' ' + self.letters[i][j]
            prnt = prnt + line.strip() + "\n"
        print(prnt)

    def lettersMatch(self, l1, l2):
        if l1 == l2:
            return True
        else:
            return False