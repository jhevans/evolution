__author__ = 'John Evans'


class Organism(object):
    _N_ORGANISMS = 0

    def __init__(self, alive=True, name=None):
        Organism._N_ORGANISMS += 1
        self._alive = alive
        if name is None:
            self.name = "organism_" + str(Organism._N_ORGANISMS)
        else:
            self.name = name

        self.genome = []

    @property
    def is_alive(self):
        return self._alive