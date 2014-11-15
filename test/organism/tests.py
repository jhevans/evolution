from unittest.case import TestCase

from organism.organism import Organism


__author__ = 'John H Evans'


class OrganismTest(TestCase):
    def setUp(self):
        self.organism = Organism()

    def test_organism_created_alive_by_default(self):
        self.assertTrue(self.organism.is_alive)

    def test_organism_can_be_created_dead(self):
        dead_organism = Organism(alive=False)
        self.assertFalse(dead_organism.is_alive)