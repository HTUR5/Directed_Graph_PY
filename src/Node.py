from typing import Any


class Node:

    def __init__(self, i, pos: tuple = None):
        self._id = i
        self.pos = pos
        self.tag = 0
        self.size_of_out = 0
        self.size_of_into = 0

    def get_pos(self):
        return self.pos

    def set_pos(self, pos: tuple):
        self.pos = pos

    def __repr__(self):
        return f'{self._id}: |edges_out| {self.size_of_out} |edges in| {self.size_of_into}'





