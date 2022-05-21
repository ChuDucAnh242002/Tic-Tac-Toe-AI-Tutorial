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
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = '0' if player == 'X' else 'X'

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best