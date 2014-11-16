from types import MethodType

from genes.exceptions import TooManyBehaviours


__author__ = 'John H Evans'


class BaseGene(object):
    _all_genes = []
    _last_id = 0

    def __init__(self):
        BaseGene._last_id += 1
        self.id = BaseGene._last_id
        BaseGene._add_gene(self)

    @classmethod
    def _add_gene(cls, new_gene):
        cls._all_genes.append(new_gene)

    @classmethod
    def get_all_genes(cls):
        return cls._all_genes


class EnablerGene(BaseGene):
    attributes = None
    _all_genes = []

    def __init__(self):
        super(EnablerGene, self).__init__()
        EnablerGene._add_gene(self)
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