from types import MethodType

__author__ = 'John Evans'


class Environment1D(object):
    def __init__(self, max_dimensions, initial_organisms):
        self._max_dimensions = max_dimensions
        self._age = 0
        self._organisms = []
        for organism in initial_organisms:
            organism_with_age = give_age(organism)
            organism_with_age_and_location = give_location(organism_with_age)
            self._organisms.append(organism_with_age_and_location)

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


def give_age(instance):
    instance.age = 0

    def increment_age(self):
        self.age += 1

    instance.increment_age = MethodType(increment_age, instance)
    return instance


def give_location(instance, initial_location=(0,)):
    instance.location = initial_location
    return instance
