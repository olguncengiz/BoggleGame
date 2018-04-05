from board import Board
import sys
import os

b = Board()
b.shuffle()

os.system('cls')
b.printBoard()

while True:
    value = input()
    os.system('cls')
    b.printBoard()
    print("\n")
    print(value)
    print(b.wordExists(value))
    print("\n")