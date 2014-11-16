from unittest.case import TestCase

from environment.environment_1d import Environment1D, give_age, give_location
from organism.organism import Organism


__author__ = 'John Evans'


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

    def test_organisms_given_age(self):
        for organism in self.env.get_organisms():
            self.assertTrue(hasattr(organism, 'age'))

    def test_organisms_given_location(self):
        for organism in self.env.get_organisms():
            self.assertTrue(hasattr(organism, 'location'))


class TestGiveAgeDecorator(TestCase):
    class TestClass(object):
        pass

    def setUp(self):
        self.decorated_instance = give_age(self.TestClass())

    def test_decorated_instance_has_age(self):
        self.assertTrue(hasattr(self.decorated_instance, 'age'))

    def test_decorated_instance_age_is_0(self):
        self.assertEqual(self.decorated_instance.age, 0)

    def test_decorated_instance_has_increment_age_method(self):
        self.assertTrue(hasattr(self.decorated_instance, 'increment_age'))

    def test_increment_age_increments_age(self):
        self.decorated_instance.increment_age()
        self.assertEqual(self.decorated_instance.age, 1)
        self.decorated_instance.increment_age()
        self.assertEqual(self.decorated_instance.age, 2)


class TestGiveLocationDecorator(TestCase):
    class TestClass(object):
        pass

    def setUp(self):
        self.decorated_instance = give_location(self.TestClass())

    def test_decorated_instance_has_location(self):
        self.assertTrue(hasattr(self.decorated_instance, 'location'))

    def test_decorated_instance_default_location_is_origin(self):
        self.assertTrue(self.decorated_instance.location, (0,))

    def test_can_set_initial_location(self):
        instance_1 = give_location(self.TestClass(), (5,))
        self.assertTrue(instance_1.location, (5,))