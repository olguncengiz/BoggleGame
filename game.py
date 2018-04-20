from gameset import GameSet
import sys
import os

class Game(object):
    def __init__(self, sets=3):
        self.gamesets = [GameSet() for x in range(sets)]
        self.currentSet = 0
        self.playing = False

    def startSet(self):
        if not self.playing:
            self.playing = True
    
    def endSet(self):
        if self.playing:
            self.playing = False
            self.currentSet += 1

    def makeMove(self, word):
        if self.playing and self.currentSet < len(self.gamesets):
            self.gamesets[currentSet].addWord(word)
            points = self.gamesets[currentSet].calculatePoints()
            return points

    def newGame(self, sets):
        self.__init__(sets)