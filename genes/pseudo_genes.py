from genes.base_genes import EnablerGene, AttributeGene
from genes.mixins import PseudoGeneMixin

__author__ = 'John H Evans'


class Mortality(AttributeGene, PseudoGeneMixin):
    attributes = {
        'alive': True,
    }

    def add_method_attributes(self):
        def die(self):
            self.alive = False

        self.register_method_attribute('die', die)


class Senescence(EnablerGene, PseudoGeneMixin):
    attributes = {
        'age': 0,
    }

    LIVE_DIE_RATIO = 9 / 10

    def __init__(self, inject__random):
        self.__random = inject__random

        super(Senescence, self).__init__()

    def add_behaviour(self):
        def increment_age(decorated_self):
            decorated_self.age += 1
            if self.__random() >= self.LIVE_DIE_RATIO:
                decorated_self.die()

        self.register_behaviour('increment_age', increment_age)