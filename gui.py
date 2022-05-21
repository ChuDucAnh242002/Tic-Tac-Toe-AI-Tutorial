from tkinter import *
from tkinter import messagebox

class GUI():
    def __init__(self, game, x_player, o_player):
        self.root = Tk()
        self.root.iconbitmap("tic-tac-toe.ico")
        self.root.title("Tic tac toe with Duc Anh")
        self.root.geometry("800x600")

        self.frame = Frame(self.root)

        self.game = game
        self.x_player = x_player
        self.o_player = o_player
        self.turn = "X"
        self.letter = "X"
        self.clicked = False

        self.xphoto = PhotoImage('X.png')
        self.ophoto = PhotoImage('0.png')
        self.labelphoto = Label(self.root, image=self.xphoto)
        
        self.btn0 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn0, 0), font=("Helvetica", 60))
        self.btn1 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn1, 1), font=("Helvetica", 60))
        self.btn2 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn2, 2), font=("Helvetica", 60))
        self.btn3 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn3, 3), font=("Helvetica", 60))
        self.btn4 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn4, 4), font=("Helvetica", 60))
        self.btn5 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn5, 5), font=("Helvetica", 60))
        self.btn6 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn6, 6), font=("Helvetica", 60))
        self.btn7 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn7, 7), font=("Helvetica", 60))
        self.btn8 = Button(self.frame, height= 1, width=3, text = " ", command = lambda: self.click(self.btn8, 8), font=("Helvetica", 60))

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

        if self.game.empty_squares() == 0 and self.game.winner() == False:
            messagebox.showinfo(message= "draw")
            return  
        if btn["text"] == " " and self.turn == "X":
            btn.config(text = "X")
            # self.label(num,self.turn)
            # btn.config(image= self.xphoto)
            self.game.gui_click(num, self.turn)
            print(self.game.board)
            if self.game.winner() == True:
                messagebox.showinfo(message= "X wins")
                return
            self.turn = "0"
            self.computer()
        
    def computer(self):
        
        if self.game.empty_squares() == 0 and self.game.winner() == False:
            messagebox.showinfo(message= "draw")
            return
        if self.turn == "0":
            block = self.o_player.get_move(self.game)
            letter = self.o_player.letter
            btn = self.find_btn(block)
            if self.game.make_move(block, letter):
                btn.config(text = "0")
                # self.label(block,self.turn)
                # btn.config(image= self.ophoto)
                print(self.game.board)
                if self.game.winner() == True:
                    messagebox.showinfo(message= "0 wins")
                    return
                self.turn = "X"      

    def label(self, num, letter):
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
