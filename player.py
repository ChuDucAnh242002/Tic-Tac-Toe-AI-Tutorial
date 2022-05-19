import math
import random

# a player class
class Player:
    def __init__(self, letter):
        """ 
        Constructor
        :param letter: o or x
        """
        self.letter = letter

    def get_move(self, game):
        pass

# a random computer player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        """
        Constructor
        :param letter: o or x
        """
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_move())
        return square

# a random human player
class HumanPlayer(Player):
    def __init__(self, letter):
        """
        Constructor
        :param letter: o or x
        """
        super().__init__(letter)

    def get_move(self, game):
        while True:
            square = int(input("Choose from 0 to 8: "))
            if square not in game.available_move():
                print ("Invalid number!")
                continue
            else :
                return square