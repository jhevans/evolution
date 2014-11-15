__author__ = 'John H Evans'


class Organism(object):
    def __init__(self, alive=True):
        self._alive = alive

    @property
    def is_alive(self):
        return self._alive