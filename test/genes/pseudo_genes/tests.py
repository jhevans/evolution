from unittest.mock import Mock

from genes.pseudo_genes import Mortality, Senescence


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


class TestSenescence(unittest.TestCase):
    def setUp(self):
        self.mock_organism = Mock()
        self.mock_pseudo = Senescence()
        self.mock_pseudo.grant_behaviour(self.mock_organism)

    def test_decorated_organism_has_age_attribute(self):
        self.assertTrue(hasattr(self.mock_organism, 'age'))

    def test_decorated_organism_has_increment_age_behaviour(self):
        self.assertTrue(hasattr(self.mock_organism, 'increment_age'))

    def test_decorated_organism_starts_at_age_0(self):
        self.assertEqual(self.mock_organism.age, 0)

    def test_increment_age(self):
        self.mock_organism.increment_age()
        self.assertEqual(self.mock_organism.age, 1)
        self.mock_organism.increment_age()
        self.assertEqual(self.mock_organism.age, 2)


if __name__ == '__main__':
    unittest.main()
