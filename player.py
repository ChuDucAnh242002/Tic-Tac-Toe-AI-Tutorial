"""
    Tutorial from Kylie Ying, 12 Beginner Python Projects - Coding Course
    Link: https://www.youtube.com/watch?v=8ext9G7xspg&t=4529s
"""

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
class DumbPlayer(Player):
    def __init__(self, letter):
        """
        Constructor
        :param letter: o or x
        """
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
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
            if square not in game.available_moves():
                print ("Invalid number!")
                continue
            else :
                return square

# AI player based on minimax algorithm
class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # if len(game.available_moves()) == 9:
        #     square = random.choice(game.available_moves())
        # else:
        square = self.minimax(game, self.letter, 0)['position']
        return square

    def minimax(self, state, player, depth):
        max_player = self.letter  
        other_player = '0' if player == 'X' else 'X'

        # Check if there is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * depth if other_player == max_player else -1 * 
                        depth}
        # Check if the match is draw
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        # Set the score to infinity and minus infinity
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  
        else:
            best = {'position': None, 'score': math.inf} 

        # play the game in availalbe move
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player, depth + 1)  

            # Reset the game state
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  

            # find the best score
            if player == max_player:  
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best