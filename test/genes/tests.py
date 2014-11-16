from unittest.mock import Mock

from genes.base_genes import EnablerGene, BaseGene
from genes.exceptions import TooManyBehaviours


__author__ = 'John H Evans'

import unittest


class TestBaseGene(unittest.TestCase):
    def setUp(self):
        self.test_gene_1 = BaseGene()
        self.test_gene_2 = BaseGene()
        self.test_gene_3 = BaseGene()

        self.test_genes = [
            self.test_gene_1,
            self.test_gene_2,
            self.test_gene_3,
        ]

    def test_all_genes_have_unique_id(self):
        ids = {gene.id for gene in self.test_genes}
        self.assertEqual(len(ids), len(self.test_genes))

    def test_get_all_genes(self):
        for gene in self.test_genes:
            self.assertIn(gene, BaseGene.get_all_genes())


class TestEnablerGene(unittest.TestCase):
    class TestEnabler(EnablerGene):
        attributes = {
            'foo': 0,
            'bar': 'the initial value of bar',
        }

        def behaviour(self):
            def frobnicate(self):
                self.foo += 1
                self.bar = 'the new value of bar'

            self.register_behaviour('frobnicate', frobnicate)

    EXPECTED_BEHAVIOUR_NAME = 'frobnicate'

    def setUp(self):
        self.mock_organism = Mock()
        self.enabler = self.TestEnabler()
        self.enabler.grant_behaviour(self.mock_organism)
        self.non_enabler = BaseGene()

        self.test_genes = [
            self.enabler,
            self.non_enabler,
        ]

    def test_attributes_given_to_organism(self):
        for attribute in self.TestEnabler.attributes:
            self.assertTrue(hasattr(self.mock_organism, attribute))

    def test_attributes_set_to_initial_value(self):
        for attribute, value in self.TestEnabler.attributes.items():
            self.assertEqual(getattr(self.mock_organism, attribute), value)

    def test_behaviour_given_to_organism(self):
        self.assertTrue(hasattr(self.mock_organism, self.EXPECTED_BEHAVIOUR_NAME))

    def test_behaviour_works(self):
        getattr(self.mock_organism, self.EXPECTED_BEHAVIOUR_NAME)()
        self.assertEqual(self.mock_organism.foo, 1)
        self.assertEqual(self.mock_organism.bar, 'the new value of bar')

    def test_maximum_1_behaviour(self):
        def bar(self):
            pass

        with self.assertRaises(TooManyBehaviours) as context_manager:
            self.enabler.register_behaviour('bar', bar)

        self.assertEqual(context_manager.exception.message, "Multiple behaviours from one gene not supported")

    def test_get_all_genes_on_base_returns_enablers(self):
        self.assertIn(self.enabler, BaseGene.get_all_genes())
        self.assertIn(self.non_enabler, BaseGene.get_all_genes())

    def test_get_all_genes_returns_only_enablers(self):
        self.assertIn(self.enabler, EnablerGene.get_all_genes())
        self.assertNotIn(self.non_enabler, EnablerGene.get_all_genes())


if __name__ == '__main__':
    unittest.main()
