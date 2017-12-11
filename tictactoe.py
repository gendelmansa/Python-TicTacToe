# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:48:04 2017

@author: shmoo
"""

class TicTacToe(object):
    def __init__(self, shape = 'x') :
        '''creates the current players shape and the board'''
        if shape == 'x' or shape == 'o':    
            self.__shape = shape
            self.__board =[['1:1','1:2','1:3'], ['2:1','2:2','2:3'], ['3:1', '3:2', '3:3']]
        else:
            raise ValueError("please put in either x or o for the shape")
        
    def __repr__(self):
        '''represents the shapes as themselves in string form'''
        return self.__shape
    def __str__(self):
        '''prints the current board state'''
        formatter_top = "row 1:  _{}|_{}_|{}_\nrow 2:  _{}|_{}_|{}_\nrow 3:   {}| {} |{} ".format(self.__board[0][0], self.__board[0][1], self.__board[0][2],self.__board[1][0], self.__board[1][1], self.__board[1][2],self.__board[2][0],self.__board[2][1],self.__board[2][2])
        return formatter_top
    def assign_shape(self, row, column):
        '''assigns an x or to given position and checks if that position is valid and within the bounds of the board'''
        if type(row) is not int:
            raise IndexError("Value not a valid number")
        elif row-1 > 2: 
            raise IndexError("Value not within board limits")
        if type(column) is not int:
            raise IndexError("Value not a valid number")
        elif column-1 > 2:
            raise IndexError("Value not a valid number")
        else:
            if self.__board[row-1][column-1] == 'x' or self.__board[row-1][column-1] == 'o':
                raise IndexError("position is already taken. Try again.")
            else:
                self.__board[row-1][column-1] = self.__shape
        
    def check_win(self):
        win_count = 0
        vert_list = [[],[],[]]
        for row in self.__board:
            if ''.join(row) == 'xxx':
                win_count +=1
            elif ''.join(row) == 'ooo':
                win_count+=1
            count = 0        
            for col in row:
                if row[count] not in vert_list:
                    vert_list[count].append(row[count])
                    count +=1
            for i in range(0,3):
                if ''.join(vert_list[i]) == 'xxx':
                    win_count+=1
                if ''.join(vert_list[i]) == 'ooo':
                    win_count+=1
            diag_check_one = [self.__board[0][0], self.__board[1][1], self.__board[2][2]]
            diag_check_two = [self.__board[0][2], self.__board[1][1], self.__board[2][0]]
            if ''.join(diag_check_one) == 'xxx' or ''.join(diag_check_two) == 'xxx':
                win_count+=1
            elif ''.join(diag_check_one) == 'ooo' or ''.join(diag_check_two) == 'ooo':
                win_count+=1
        if win_count>0:
            return True
        elif win_count == 0:
            return False
    def get_player_shape(self):
        if self.__shape == 'x':
            return 'x'
        elif self.__shape == 'o':
            return 'o'
    def switch_player_shape(self):
        if self.__shape == 'x':
            self.__shape = 'o'
        elif self.__shape == 'o':
            self.__shape = 'x'
    def restart_game(self):
        self.__board =[['1','2','3'], ['1','2','3'], ['1', '2', '3']]
        
def main():
    n = 0
    while n == 0 :
       try:
           player1 = input("Input shape either 'x' or 'o' to decide who goes first: ")
           game = TicTacToe(player1)
           n+=1
       except ValueError as x:
           print(x)
           
        
    
    print("Welcome to TicTacToe! below is a reference to the board.")
    print(game)
    print("to input a move put in the row number and then the column number")
    playagain = 'yes'
    count = 0
    while playagain != 'no':
        try:
            move_row = int(input("please put in a row: "))
            move_col = int(input("please put in a column: "))      
            game.assign_shape(move_row, move_col)
            win = game.check_win()
            print(game)
            if win == True:
                count = -1
                current_player = game.get_player_shape()
                print("{} wins!".format(current_player))
                playagain = input("Would you like to play again: ")
                if playagain == 'yes':
                    game.restart_game()
            if count == 9:
                playagain = input("Cats game, would you like to play again?: ")
                if playagain == 'yes':
                    game.restart_game()
            game.switch_player_shape()
            count+=1
        except IndexError as x:
            print(x)
main()
                
                