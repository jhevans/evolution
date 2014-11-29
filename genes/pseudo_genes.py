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