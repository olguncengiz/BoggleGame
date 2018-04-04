import unittest
from board import Board
    
class TestBoard(unittest.TestCase):    
    def setUp(self):
        self.board = Board()
    
    def test_board(self):
        print("\n")
        print("Creating Board...")
        self.assertEqual(len(self.board.letters), 0)
        
        print("Shuffling Board...")
        self.board.shuffle()

        print("Printing Board...")
        self.board.printBoard()

        word = self.board.letters[2][2]
        print("Word is %s" % word)

        print("Found At [2][2]")
        self.assertEqual(self.board.lettersMatch(word, self.board.letters[2][2]), True)

        self.assertEqual(self.board.wordExists(word), True)
        word = self.board.letters[0][0] + self.board.letters[0][1] + self.board.letters[0][2] + self.board.letters[1][2]
        print("Word is %s" % word)

        print("Found At [0][0]-[0][1]-[0][2]-[1][2]")
        self.assertEqual(self.board.wordExists(word), True)

        word = self.board.letters[0][0] + self.board.letters[3][3] + self.board.letters[0][3] + self.board.letters[3][0]
        print("Word is %s" % word)

        print("Not Found!")
        self.assertEqual(self.board.wordExists(word), False)

        self.assertEqual(len(self.board.letters), 4)
        self.assertEqual(len(self.board.letters[0]), 4)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBoard)
    unittest.TextTestRunner(verbosity=2).run(suite)