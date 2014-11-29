from genes.base_genes import EnablerGene
from genes.mixins import PseudoGeneMixin

__author__ = 'John H Evans'


class Mortality(EnablerGene, PseudoGeneMixin):
    attributes = {
        'alive': True,
    }

    def behaviour(self):
        def die(self):
            self.alive = False

        self.register_behaviour('die', die)


class Senescence(EnablerGene, PseudoGeneMixin):
    attributes = {
        'age': 0,
    }

    def behaviour(self):
        def increment_age(self):
            self.age += 1

        self.register_behaviour('increment_age', increment_age)