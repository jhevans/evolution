__author__ = 'John Evans'


class Environment1D(object):
    def __init__(self, max_dimensions, initial_organisms):
        self._max_dimensions = max_dimensions
        self._age = 0
        self._organisms = []
        for organism in initial_organisms:
            self._organisms.append(organism)

    def get_max_dimensions(self):
        return self._max_dimensions

    def get_age(self):
        return self._age

    def increment_age(self):
        self._age += 1
        for organism in self._organisms:
            organism.increment_age()

    def get_organisms(self):
        return self._organisms