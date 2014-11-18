from unittest.case import TestCase

from organism.organism import Organism


__author__ = 'John Evans'


class OrganismTest(TestCase):
    def setUp(self):
        self.context = {}
        self.organism = Organism()

    def test_organism_created_alive_by_default(self):
        self.assertTrue(self.organism.is_alive)

    def test_organism_can_be_created_dead(self):
        dead_organism = Organism(alive=False)
        self.assertFalse(dead_organism.is_alive)

    def test_organism_can_be_given_name(self):
        named_organism = Organism(name="Alfred")
        self.assertEqual(named_organism.name, "Alfred")

    def test_organism_given_unique_default_name(self):
        self.assertTrue(self.organism.name)
        organism_1 = Organism()
        organism_2 = Organism()
        self.assertNotEqual(self.organism.name, organism_1.name)
        self.assertNotEqual(self.organism.name, organism_2.name)
        self.assertNotEqual(organism_1.name, organism_2.name)

    def test_undecorated_organism_has_empty_genome(self):
        self.assertEqual(self.organism.genome, [])

    def test_set_context(self):
        self.organism.set_context(self.context)
        self.assertEqual(self.organism._context, self.context)

    def test_get_context(self):
        self.assertIsNone(self.organism.get_context())
        self.organism.set_context(self.context)
        self.assertEqual(self.organism.get_context(), self.context)
