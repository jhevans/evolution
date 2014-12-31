from genes.base_genes import EnablerGene, AttributeGene
from genes.mixins import PseudoGeneMixin

__author__ = 'John H Evans'


class Mortality(AttributeGene, PseudoGeneMixin):
    attributes = {
        'alive': True,
    }

    def add_method_attributes(self):
        def die(decorated_self):
            self.info('Organism "%s" died' % decorated_self.name)
            decorated_self.alive = False

        self.register_method_attribute('die', die)


class Senescence(EnablerGene, PseudoGeneMixin):
    attributes = {
        'age': 0,
        'died_age': None,
    }

    LIVE_DIE_RATIO = 99 / 100

    def __init__(self, inject__random):
        self.__random = inject__random

        super(Senescence, self).__init__()

    def add_behaviour(self):
        def increment_age(decorated_self):
            decorated_self.age += 1
            self.debug(
                'increase_age() called on Organism "%s", current age is %i' % (decorated_self.name, decorated_self.age))
            if decorated_self.died_age is None:
                if self.__random() >= self.LIVE_DIE_RATIO:
                    decorated_self.die()
                    decorated_self.died_age = decorated_self.age

        self.register_behaviour('increment_age', increment_age)