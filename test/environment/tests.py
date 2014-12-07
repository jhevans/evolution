from unittest.case import TestCase, skip

from environment.environment_1d import Environment1D
from organism.organism import Organism


__author__ = 'John Evans'


@skip(
    'The environments responsibilities have changed since this was written, needs a complete redesign.  Also why no mocking!?')
class TestEnvironment1D(TestCase):
    DEFAULT_DIMENSIONS = (100,)
    INITIAL_ORGANISMS = [
        Organism(name='Tom'),
        Organism(name='Dick'),
        Organism(name='Harry'),
        Organism(alive=False, name='Deadun'),
    ]

    def setUp(self):
        self.env = Environment1D(self.DEFAULT_DIMENSIONS, self.INITIAL_ORGANISMS)

    def test_new_env_has_age_0(self):
        self.assertEqual(self.env.get_age(), 0)

    def test_get_max_dimensions(self):
        self.assertEqual(self.env.get_max_dimensions(), self.DEFAULT_DIMENSIONS)

    def test_increment_age_increases_environment_age(self):
        self.env.increment_age()
        self.assertEqual(self.env.get_age(), 1)
        self.env.increment_age()
        self.assertEqual(self.env.get_age(), 2)

    def test_increment_age_calls_increment_age_on_organisms(self):
        for organism in self.env.get_organisms():
            self.assertEqual(organism.age, 0)
        self.env.increment_age()
        for organism in self.env.get_organisms():
            self.assertEqual(organism.age, 1)

    def test_get_organisms_returns_named_organisms(self):
        for i, organism in enumerate(self.env.get_organisms()):
            self.assertEqual(organism.name, self.INITIAL_ORGANISMS[i].name)
