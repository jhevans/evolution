from unittest.mock import Mock

from genes.pseudo_genes import Mortality, Senescence
from organism.organism import Organism


__author__ = 'John H Evans'

import unittest


class TestMortality(unittest.TestCase):
    def setUp(self):
        self.mock_organism = Mock(spec=Organism())
        self.mortality_pseudo = Mortality()
        self.mortality_pseudo.decorate(self.mock_organism)

    def test_decorated_organism_has_alive_attribute(self):
        self.assertTrue(hasattr(self.mock_organism, 'alive'))

    def test_decorated_organism_has_die_behaviour(self):
        self.assertTrue(hasattr(self.mock_organism, 'die'))

    def test_organism_starts_off_alive(self):
        self.assertTrue(self.mock_organism.alive)

    def test_die(self):
        self.mock_organism.die()
        self.assertFalse(self.mock_organism.alive)


class TestSenescence(unittest.TestCase):
    def setUp(self):
        self.mock_organism = Mock(spec=Organism())
        self.mock_organism.die = Mock()
        self.mock_random = Mock(return_value=0.5)
        self.senescence = Senescence(self.mock_random)
        self.senescence.decorate(self.mock_organism)

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

    def test_organism_dies_when_random_returns_LIVE_DIE_RATIO(self):
        self.mock_random.return_value = Senescence.LIVE_DIE_RATIO
        self.mock_organism.increment_age()
        self.assertTrue(self.mock_organism.die.called)

    def test_organism_dies_when_random_returns_1(self):
        self.mock_random.return_value = 1.0
        self.mock_organism.increment_age()
        self.assertTrue(self.mock_organism.die.called)

    def test_organism_lives_when_random_returns_just_less_than_LIVE_DIE_RATIO(self):
        self.mock_random.return_value = Senescence.LIVE_DIE_RATIO - 0.0001
        self.mock_organism.increment_age()
        self.assertFalse(self.mock_organism.die.called)

    def test_organism_lives_when_random_returns_0(self):
        self.mock_random.return_value = 0.0
        self.mock_organism.increment_age()
        self.assertFalse(self.mock_organism.die.called)

    def test_decorated_organism_has_increment_age_attribute(self):
        self.assertTrue(hasattr(self.mock_organism, 'died_age'))

    def test_organism_died_age_starts_at_None(self):
        self.assertEqual(self.mock_organism.died_age, None)

    def test_organism_died_age_not_set_when_not_dead(self):
        self.mock_random.return_value = 0
        self.mock_organism.increment_age()
        self.assertEqual(self.mock_organism.died_age, None)

    def test_organism_has_died_age_set_on_death(self):
        self.mock_random.return_value = 0
        self.mock_organism.increment_age()
        self.mock_random.return_value = 1
        self.mock_organism.increment_age()
        self.assertEqual(self.mock_organism.died_age, 2)

    def test_organism_died_age_does_not_increase_when_dead(self):
        self.mock_random.return_value = 1
        self.mock_organism.increment_age()
        self.mock_organism.increment_age()
        self.assertEqual(self.mock_organism.died_age, 1)


if __name__ == '__main__':
    unittest.main()
