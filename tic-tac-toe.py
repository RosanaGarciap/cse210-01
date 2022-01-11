'''
Assignment: Game Tic-Tac-Toe
 String Version
Author: Rosana Garcia
Course: CSE 210
'''
class Board():
    def __init__(self):
        self.board = "1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9"
        #             0 2 4        12 14 16      24 26 28
    def display_board(self):
        print(self.board+"\n")
        
    def update(self,new_board):
        self.board = new_board

class Game():
    # class constructor
    def __init__(self):
        self.counter = 9
        self.board = Board()

    def change_board(self, pos, value):
        new_board = self.board.board.replace(pos,value)
        self.board.update(new_board)
        self.board.display_board()

    def win_player(self):
        if((self.board.board[0]==self.board.board[2]==self.board.board[4]) or (self.board.board[0]==self.board.board[12]==self.board.board[24]) or (self.board.board[12]==self.board.board[14]==self.board.board[16]) or (self.board.board[24]==self.board.board[26]==self.board.board[28]) or (self.board.board[0]==self.board.board[2]==self.board.board[4]) or (self.board.board[2]==self.board.board[14]==self.board.board[26]) or (self.board.board[4]==self.board.board[16]==self.board.board[28])):
             return True

    def keep_playing(self):
        while((self.counter!=0) and not(self.win_player())):
            move = 0
            if (self.counter%2 != 0):
                move = input("x's turn to choose a square (1-9): ")
                self.change_board(move, 'x')
            else: 
                move = input("0's turn to choose a square (1-9): ") 
                self.change_board(move, 'o')
            self.counter = self.counter - 1 
        print("Good game. Thanks for playing!")

    def start_playing(self):
        self.board.display_board()
        self.keep_playing()

def main():
    play = Game()
    play.start_playing()
main()
