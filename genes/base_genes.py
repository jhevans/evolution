from types import MethodType

from genes.exceptions import TooManyBehaviours


__author__ = 'John H Evans'


class BaseGene(object):
    pass


class EnablerGene(BaseGene):
    attributes = None

    def __init__(self):
        self.behaviours = {}
        self.behaviour()

    def behaviour(self):
        pass

    def grant_behaviour(self, instance):
        if self.attributes is not None:
            for attribute, value in self.attributes.items():
                setattr(instance, attribute, value)

        for name, behaviour in self.behaviours.items():
            setattr(instance, name, MethodType(behaviour, instance))

    def register_behaviour(self, name, behaviour):
        if len(self.behaviours) >= 1:
            raise TooManyBehaviours()
        self.behaviours[name] = behaviour