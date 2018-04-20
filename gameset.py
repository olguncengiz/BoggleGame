from board import Board
import functools

class GameSet(object):
    def __init__(self):
        self.board = Board()
        self.board.shuffle()
        self.words = list()

    def printBoard(self):
        self.board.printBoard()

    def addWord(self, word):
        if (word not in self.words) and (self.board.isValid(word)):
            self.words.append(word)

    def calculatePoints(self):
        points = 0
        for i in range(len(self.words)):
            points += ((len(self.words[i]) - 3) * 2) + 1
        return points
