from unittest.case import TestCase

from environment.environment_1d import Environment1D


__author__ = 'John H Evans'


class TestEnvironment1D(TestCase):
    DEFAULT_DIMENSIONS = (100,)
    INITIAL_ORGANISMS = []

    def setUp(self):
        self.env = Environment1D(self.DEFAULT_DIMENSIONS, [])

    def test_new_env_has_age_0(self):
        self.assertEqual(self.env.get_age(), 0)

    def test_get_max_dimensions(self):
        self.assertEqual(self.env.get_max_dimensions(), self.DEFAULT_DIMENSIONS)

    def test_increment_age(self):
        self.env.increment_age()
        self.assertEqual(self.env.get_age(), 1)
        self.env.increment_age()
        self.assertEqual(self.env.get_age(), 2)

    def test_get_organisms(self):
        self.assertEqual(self.env.get_organisms(), self.INITIAL_ORGANISMS)