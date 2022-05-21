
from player import DumbPlayer, HumanPlayer, AIPlayer
from gui import GUI

class TicTacToe():
    def __init__(self) :
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        # Create a board in list form
        return [' ' for _ in range(9)]
    
    def print_board(self):
        for i in range(0,8,3):
            print(f"| {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} |")
        print()

    @staticmethod
    def print_board_nums():
        for i in range(0,8,3):
            print(f"| {i} | {i+1} | {i+2} |")
        print()

    def available_moves(self):
        moves = []
        for i in range(0,9):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner():
                self.current_winner = letter
            return True
        return False
    
    def winner(self):
        # Verticle
        for i in range(0,7,3):
            if self.board[i] == " ":
                continue
            if self.board[i] == self.board[i+1] and self.board[i] == self.board[i+2]:
                return True

        # Horizontal
        for i in range(0,3):
            if self.board[i] == " ":
                continue
            if self.board[i] == self.board[i+3] and self.board[i] == self.board[i+6]:
                return True
        
        # Wings
        k = self.board[4]
        if k == " ":
            return False
        elif (k == self.board[0] and k == self.board[8]) or (k == self.board[2] and k == self.board[6]):
            return True

        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def gui_click(self, num, turn):
            self.board[num] = turn


def play(game, x_player, o_player):
    turn = "X"
    letter = "X"
    game.print_board_nums()
    while game.empty_squares():
        if turn == "X":
            block = x_player.get_move(game)
            letter = x_player.letter

        elif turn == "0":
            block = o_player.get_move(game)
            letter = o_player.letter
        
        if game.make_move(block, letter):
            game.print_board()

            if game.current_winner:
                print( letter + " wins")
                return game.current_winner

        if turn == "X":
            turn = "0"
        else : turn = "X"
    print("Draw")
    return game.current_winner
    
def main():

    x_player = AIPlayer('X')
    o_player = AIPlayer('0')
    game = TicTacToe()
    # play(game, x_player, o_player)
    GUI(game, x_player, o_player)
    

if __name__ == '__main__':
    main()