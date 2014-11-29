from unittest.mock import Mock

from genes.pseudo_genes import Mortality


__author__ = 'John H Evans'

import unittest


class TestMortality(unittest.TestCase):
    def setUp(self):
        self.mock_organism = Mock()
        self.mortality_pseudo = Mortality()
        self.mortality_pseudo.grant_behaviour(self.mock_organism)

    def test_decorated_organism_has_alive_attribute(self):
        self.assertTrue(hasattr(self.mock_organism, 'is_alive'))

    def test_decorated_organism_has_die_behaviour(self):
        self.assertTrue(hasattr(self.mock_organism, 'die'))

    def test_organism_starts_off_alive(self):
        self.assertTrue(self.mock_organism.alive)

    def test_die(self):
        self.mock_organism.die()
        self.assertFalse(self.mock_organism.alive)


if __name__ == '__main__':
    unittest.main()
