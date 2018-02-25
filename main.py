import Chess
import tkinter

"""
The main function 
"""

if __name__ == '__main__':
    window = tkinter.Tk()
    gui_chess_board = Chess.Chess_Board_Frame(window)
    gui_chess_board.pack()
    window.mainloop()
