# -*- coding: utf-8 -*-
from Car import *
from collections import namedtuple, deque
from copy import deepcopy

Position = namedtuple('Position', 'y x') 

class Movement():
    """
    Represents car moved to the distance
    Movement(car name,distance)
    """
    def __init__(self, obj, direction):
        """ :type obj: str, :type direction: int """
        self.obj = obj
        self.direction = direction

    def __str__(self):
        return "{} {:+}".format(self.obj, self.direction)


class Board():
    """
    Represents Board with cars, finish cell, with, height, etc.
    """
    def __init__(self, input):
        """
        Constructor for the board
        Represents cars, finish, width, height and moves
        :param input: input grid
        :type input: str
        """
        self.cars = dict()
        self.finish = None
        self.width = 0
        self.height = 0
        self.moves = []
        self.parsing(input)

        assert self.finish is not None, "There's no finish on the board."
        assert 'r' in self.cars, "There is no red car on the board."

    def parsing(self, input):
        """
        Transform input string to board

        :param input: input board
        :type input: str
        :return: None
        """
        lines = list(map(lambda l: l.strip(), input.strip().split('\n')))
        self.height = len(lines)
        prev = '.'
        for i, line in enumerate(lines):
            width = len(line.replace('>', ''))
            if self.width == 0:
                self.width = width
            else:
                assert  self.width == width, "Check equality"
            for j, char in enumerate(line):
                if char == '.':
                    pass
                elif char == '>':
                    self.finish = (i, j)
                elif char not in self.cars:
                    self.cars[char] = Car(char, Position(i, j), 1)
                else:
                    self.cars[char].size += 1
                    self.cars[char].is_horizontal = (char == prev)
                prev = char

    def get_position_contents(self, pos):
        """
        Return Car object on given position and if there's no car return None

        :param pos: position of the car
        :type pos: namedtuple
        :return: car at given position
        :rtype: Car object <Car.Car instance at ...>
        """
        for k, piece in self.cars.items():
            if (piece.pos.x <= pos.x <= piece.end.x 
              and piece.pos.y <= pos.y <= piece.end.y):
                return piece
        return None

    def get_child_states(self):
        """
        Returns a list of child states possible.
        
        :Return: list of objects
        :rtype: list
        :Example:
        >>> board = '''GG...Y
               V..B.Y
               VrrB.Y>
               V..B..
               O...HH
               O.LLL.'''
        >>> bb=Board(board)
        >>> bb.get_child_states()
        [<rh.Board object at 0x7f63886bba58>, <rh.Board object at 0x7f63886d3128>, <rh.Board object at 0x7f63886d3358>, <rh.Board object at 0x7f63886d3588>, <rh.Board object at 0x7f63886d37b8>, <rh.Board object at 0x7f63886d39e8>, <rh.Board object at 0x7f63886d3c18>, <rh.Board object at 0x7f63886d3e48>, <rh.Board object at 0x7f63886e3588>, <rh.Board object at 0x7f63886e3f28>, <rh.Board object at 0x7f63886e30f0>]
        """
        states = []
        max_moves = max(self.width, self.height)
        for k, piece in self.cars.items():
            for direction in (-1,1):
                offset = direction
                is_valid = True
                while is_valid:
                    pos = piece.get_new_pos(offset)
                    is_valid = self.is_valid_position(pos)
                    if is_valid:
                        states.append(self.make_state(Movement(k, offset)))
                    offset += direction
        return states

    def is_valid_position(self, pos):
        """
        Checks if given as argument position is valid : inside of board and there's no
        car on this position.
        
        :param pos: position of type Position(x,y)
        :type pos: namedtuple
        :Return: True of False
        :rtype: bool

        :Example:
        >>> board = '''GG...Y
               V..B.Y
               VrrB.Y>
               V..B..
               O...HH
               O.LLL.'''
        >>> bb=Board(board)
        >>> bb.is_valid_position(Position(0,1))
        False
        >>> bb.is_valid_position(Position(0,2))
        True
        
        """
        if 0 <= pos.y < self.height and 0 <= pos.x < self.width:
            if self.get_position_contents(pos) is None:
                return True
        return False

    def make_state(self, move):
        """
        Returns created state for moved car

        :param move: represents movement
        :type move: object of class Movement
        :return: new state of moved car
        :rtype: Board instance <__main__.Board instance at ...>
        """
        state = deepcopy(self)
        state.move_car(move)
        return state

    def move_car(self, move):
        """
        Moves car according to given move Movement(car name, direction)

        :param move: represents movement
        :type move: object of class Movement
        :return: None
        """
        self.moves.append(move)
        car = self.cars[move.obj]
        car.move(move.direction)

    def __str__(self):
        state = []
        for key in sorted(self.cars.keys()):
            state.append("{}({},{},{})".format(key, self.cars[key].pos.y, 
                self.cars[key].pos.x, 0 if self.cars[key].is_horizontal else 1))
        return ":".join(state)

