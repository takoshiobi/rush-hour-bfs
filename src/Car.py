from Board import *
from collections import *
from copy import deepcopy

Position = namedtuple('Position', 'y x')

class Car():
    """
    Car construcor : size, init position, label (name), orientation (is_horizontal:True/False)
    """
    def __init__(self, name='_', pos=Position(0,0), size=1, is_horizontal=True):
        self.name = name
        self.pos = pos
        self.size = size
        self.is_horizontal = is_horizontal
        
    def fin(self):
        """
        Returns car final position
        
        :return: position as Position(x,y)
        :rtype: namedtuple
        """
        y, x = self.pos
        if self.is_horizontal:
            x += self.size - 1
        else:
            y += self.size - 1
        return Position(y, x)

    end=property(fin)

    def get_new_pos(self, distance):
        """
        Car possible position according to given distance

        :return: new possible position
        :rtype: nametuple
        """
        y, x = self.pos
        if distance > 0:
            y, x = self.end
        if self.is_horizontal:
            x += distance
        else:
            y += distance
        return Position(y, x)

    def move(self, distance):
        """
        Moves car for the given distance

        :return: None
        """
        y, x = self.pos
        if self.is_horizontal:
            x += distance
        else:
            y += distance
        self.pos = Position(y, x)

    def __str__(self):
        return "{} {} {} {}".format(    
            self.name, self.pos, self.size, self.is_horizontal)
