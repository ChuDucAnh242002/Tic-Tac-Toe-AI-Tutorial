"""
    Author : Chu Duc Anh
    Github : https://github.com/ChuDucAnh242002
    GUI that show tic tac toe game using tkinter module
"""

from tkinter import *
from tkinter import messagebox

class GUI():
    def __init__(self, game, x_player, o_player):

        # main window
        self.root = Tk()
        self.root.iconbitmap("tic-tac-toe.ico")
        self.root.title("Tic tac toe with Duc Anh")
        self.root.geometry("800x600")
        self.frame = Frame(self.root)

        # get game, x and o player from game.py
        self.game = game
        self.x_player = x_player
        self.o_player = o_player
        self.turn = "X"

        # load image
        self.xphoto = PhotoImage('X.png')
        self.ophoto = PhotoImage('0.png')
        self.labelphoto = Label(self.root, image=self.xphoto)
        
        # Button for player
        self.btn0 = Button(self.frame, height= 1, width=3, text = " ", bg ="#198bb7", command = lambda: self.click(self.btn0, 0), font=("Helvetica", 60) )
        self.btn1 = Button(self.frame, height= 1, width=3, text = " ", bg ="#48b8d7", command = lambda: self.click(self.btn1, 1), font=("Helvetica", 60))
        self.btn2 = Button(self.frame, height= 1, width=3, text = " ", bg ="#7bcee3", command = lambda: self.click(self.btn2, 2), font=("Helvetica", 60))
        self.btn3 = Button(self.frame, height= 1, width=3, text = " ", bg ="#1b8fbb",command = lambda: self.click(self.btn3, 3), font=("Helvetica", 60))
        self.btn4 = Button(self.frame, height= 1, width=3, text = " ", bg ="#30a7ca", command = lambda: self.click(self.btn4, 4), font=("Helvetica", 60))
        self.btn5 = Button(self.frame, height= 1, width=3, text = " ", bg ="#8ad8e2", command = lambda: self.click(self.btn5, 5), font=("Helvetica", 60))
        self.btn6 = Button(self.frame, height= 1, width=3, text = " ", bg ="#1584b7", command = lambda: self.click(self.btn6, 6), font=("Helvetica", 60))
        self.btn7 = Button(self.frame, height= 1, width=3, text = " ", bg ="#2ea7ca", command = lambda: self.click(self.btn7, 7), font=("Helvetica", 60))
        self.btn8 = Button(self.frame, height= 1, width=3, text = " ", bg ="#84d5e6", command = lambda: self.click(self.btn8, 8), font=("Helvetica", 60))

        # Button grids
        self.btn0.grid(row=0, column=0, columnspan=1, padx=5, pady= 10)
        self.btn1.grid(row=0, column=1, columnspan=1, padx=5, pady= 10)
        self.btn2.grid(row=0, column=2, columnspan=1, padx=5, pady= 10)
        self.btn3.grid(row=1, column=0, columnspan=1, padx=5, pady= 10)
        self.btn4.grid(row=1, column=1, columnspan=1, padx=5, pady= 10)
        self.btn5.grid(row=1, column=2, columnspan=1, padx=5, pady= 10)
        self.btn6.grid(row=2, column=0, columnspan=1, padx=5, pady= 10)
        self.btn7.grid(row=2, column=1, columnspan=1, padx=5, pady= 10)
        self.btn8.grid(row=2, column=2, columnspan=1, padx=5, pady= 10)

        self.frame.pack(expand= True)
        self.frame.bind("<Leave>", self.quit)
        
        self.root.mainloop()

    def click(self, btn, num):
        """
            Only human player can click and only on X turn
        """

        # Draw situation
        if self.game.empty_squares() == 0 and self.game.winner() == False:
            messagebox.showinfo(title = "Draw", message= "Try better next time!")
            return  

        # X turn
        if btn["text"] == " " and self.turn == "X":
            btn.config(text = "X")
            self.game.gui_click(num, self.turn)

            # X win situation
            if self.game.winner() == True:
                messagebox.showinfo(title ="X wins", message= "How lucky is that?")
                return
            self.turn = "0"

            # change to computer turn
            self.computer()
        
    def computer(self):

        """
            Computer will be played by AI using minimax algorithm. It is in game.py
        """

        # Draw situation
        if self.game.empty_squares() == 0 and self.game.winner() == False:
            messagebox.showinfo(title = "Draw", message= "Try better next time!")
            return
            
        # 0 turn
        if self.turn == "0":
            block = self.o_player.get_move(self.game)
            letter = self.o_player.letter
            btn = self.find_btn(block)
            if self.game.make_move(block, letter):
                btn.config(text = "0")

                # 0 wins
                if self.game.winner() == True:
                    messagebox.showinfo(title= "0 wins", message= "Why you are so chicken?")
                    return
                self.turn = "X"      

    def label(self, num, letter):
        """
        This function was meant to put the label on top of button.
        """
        if letter == "X":
            self.labelphoto.config(image= self.xphoto)
        elif letter == "0":
            self.labelphoto.config(image= self.ophoto)
        if num == 0:
            self.labelphoto.grid(row=0, column=0, columnspan=1, padx=5, pady= 10)
        if num == 1:
            self.labelphoto.grid(row=0, column=1, columnspan=1, padx=5, pady= 10)
        if num == 2:
            self.labelphoto.grid(row=0, column=2, columnspan=1, padx=5, pady= 10)
        if num == 3:
            self.labelphoto.grid(row=1, column=0, columnspan=1, padx=5, pady= 10)
        if num == 4:
            self.labelphoto.grid(row=1, column=1, columnspan=1, padx=5, pady= 10)
        if num == 5:
            self.labelphoto.grid(row=1, column=2, columnspan=1, padx=5, pady= 10)
        if num == 6:
            self.labelphoto.grid(row=2, column=0, columnspan=1, padx=5, pady= 10)
        if num == 7:
            self.labelphoto.grid(row=2, column=1, columnspan=1, padx=5, pady= 10)
        if num == 8:
            self.labelphoto.grid(row=2, column=2, columnspan=1, padx=5, pady= 10)
            
    def find_btn(self, num):
        """
            Finding button by number
        """
        if num == 0 : return self.btn0
        if num == 1 : return self.btn1
        if num == 2 : return self.btn2
        if num == 3 : return self.btn3
        if num == 4 : return self.btn4
        if num == 5 : return self.btn5
        if num == 6 : return self.btn6
        if num == 7 : return self.btn7
        if num == 8 : return self.btn8

    def quit(self):
        self.root.destroy()
