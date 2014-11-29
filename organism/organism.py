__author__ = 'John Evans'


class Organism(object):
    _N_ORGANISMS = 0

    def __init__(self, alive=True, name=None):
        Organism._N_ORGANISMS += 1
        self._context = None
        if name is None:
            self.name = "organism_" + str(Organism._N_ORGANISMS)
        else:
            self.name = name

        self.genome = []

    def set_context(self, context):
        self._context = context

    def get_context(self):
        return self._context