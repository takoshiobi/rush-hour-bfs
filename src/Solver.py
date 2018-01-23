# -*- coding: utf-8 -*-
from Board import *
from Car import *

from collections import *
from copy import deepcopy

Position = namedtuple('Position', 'y x') 

class BoardSolver():
    """
    Creates and displays the grid
    """
    def __init__(self, input):
        self.win = None
        self.et = set()
        self.etats = deque()

        self.etats.append(Board(input))
        self.et.add(str(self.etats[0]))

    def solve(self):
        """
        Rush hour solver
        
        :Return: None
        """
        while self.etats:
            state = self.etats.popleft()
            if state.cars['r'].get_new_pos(1) == state.finish:
                state.moves[-1].direction += 1
                self.win = state
                return
            c_s = state.get_child_states()
            for cs in c_s:
                it = str(cs)
                if it not in self.et:
                    self.et.add(it)
                    self.etats.append(cs)

        

    def display(self):
        """
        Display possible solution if game is unsovable print : unsolvable grid

        :return: None
        """
        if self.win is None:
            print ("Unsolvable game.")
        else:
            for step in self.win.moves:
                print(step)

    def winner_car_positions_as_dict(self):
        """
        Returns dict of type {'car name': (Position(y, x),size,orientation)}

        :return: dict of positions for cars
        :rtype: dict
        """
        d=self.win.cars
        if self.win is None:
            return "Game is unsolvable"
        else:
            for el in d:
               d[el]=(d[el].pos,d[el].size,d[el].is_horizontal)
        return d
                
            

    def winner_car_matrix(self):
        """
        Put solution into the matrix

        :Return: list of lists with cars placed in final state
        :rtype: list
        """
        matrix=[[' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ']]
        pos=self.winner_car_positions_as_dict()
        for car in pos:
            matrix[pos[car][0][0]][pos[car][0][1]]=car
            orientation = pos[car][2]
            size=pos[car][1]
            if orientation==True:
                for i in range(size):
                    matrix[pos[car][0][0]][pos[car][0][1]+i]=car
            else:
                for i in range(size):
                    matrix[pos[car][0][0]+i][pos[car][0][1]]=car
        return matrix


        
