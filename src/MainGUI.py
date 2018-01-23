import tkinter as tk
from Solver import *

#cars from A to Z (uppercase chars only)
dict_ = {'r': 'red',
         'Y': '#d008ff',
         'A': 'cyan',
         'B': '#00cca5',
         'C': 'gold',
         'D': 'green2',
         'E': 'tan1',
         'F': 'deep pink',
         'G': 'bisque2',
         'H': '#00ff14',
         'I': 'orange',
         'J': 'khaki1',
         'K': 'purple1',
         'O': 'Lightblue3',
         'P': 'salmon',
         'Q': 'lemon chiffon',
         'R': 'OliveDrab2',
         'V': 'violet',
         'L': 'white',
         'M': '#89d75d',
         'N': '#5d89d7',
         'S': '#5dc6d7',
         'T': '#d75d89',
         'U': '#5dd7b5',
         'W': '#d9bfc1',
         'X': '#fc9ca3',
         'Z': '#fcbd9c'}

class InitialBoard(tk.Tk):
    """
    Creates the initial board
    """
    def __init__(self, board):
        tk.Tk.__init__(self)
        self.title("Rush Hour Initial Board")
        t = Table(self, board, 8, 8)
        t.pack(side="top", fill="x")

class Solved(tk.Tk):
    """
    Creates the solved board
    """
    def __init__(self,board):
        tk.Tk.__init__(self)
        self.title("Rush Hour Solved")
        b=Table(self,board,8,8)
        b.pack(side="top", fill="x")

class Table(tk.Frame):
    """
    Create Frame
    """
    def __init__(self, parent, board, rows=8, columns=8):
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for i in range(rows):
            current_row = []
            for j in range(columns):     
                if (i >= 1 and i <=6 and j >= 1 and j <=6):
                    vehicleId = board[i-1][j-1]
                    if (vehicleId != ' '):              
                        label = tk.Label(self, text=vehicleId, bg=dict_[vehicleId], borderwidth=1, width=10)
                    else:
                        label = tk.Label(self, text=vehicleId, bg='#888888', borderwidth=1, width=10)                       
                elif (i == 3 and j == 7):
                    label = tk.Label(self, text="finish", bg='red', borderwidth=1, width=10)
                else:
                    label = tk.Label(self, text="", bg='#b2b2b2', 
                                 borderwidth=0, width=10)
                label.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                current_row.append(label)
            self._widgets.append(current_row)
        for j in range(columns):
            self.grid_columnconfigure(j, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

if __name__ == "__main__":
    import sys

    def transform(board):
        """
        Transform text file to the board of type list of lists

        :param board: text file representing board
        :return: board
        :rtype: list of lists
        """
        with open(board) as f:
            content = f.readlines() 
        content = [list(x.strip().replace("."," ")) for x in content]
        
        return content          
        
    def readf(file):
        """
        Read input file and return it as a string

        :param file: text file representing board
        :return: string of text file
        :rtype: str
        """
        with open(file) as f:
            data=f.read()
        return data

    n = str(sys.argv[1])
    game=transform(n)
    app=InitialBoard(game)
    board=readf(n)
    p=BoardSolver(board)
    p.solve()
    solution=p.winner_car_matrix()
    app2=Solved(solution)

    app.mainloop()
    app2.mainloop()
    
    
    
