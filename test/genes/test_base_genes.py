from unittest.case import skip
from unittest.mock import Mock, patch

from genes.base_genes import EnablerGene, BaseGene, AttributeGene
from genes.exceptions import TooManyBehaviours, BehaviourNotImplemented
from organism.organism import Organism


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

    @patch('logging.getLogger')
    def test_add_gene_logs_debug_message(self, mock_getLogger):
        mock_logger = Mock()
        mock_getLogger.return_value = mock_logger
        BaseGene()
        mock_logger.debug.assert_called_with('Adding gene BaseGene')


class TestAttributeGene(unittest.TestCase):
    class TestAttributeGene(AttributeGene):
        attributes = {
            'foo': 0,
            'bar': 'the initial value of bar',
        }

        def add_method_attributes(self):
            def frobnicate(self):
                self.foo += 1
                self.bar = 'the new value of bar'

            self.register_method_attribute('frobnicate', frobnicate)

    def setUp(self):
        self.mock_organism = Mock(spec=Organism)
        self.attribute_gene = self.TestAttributeGene()
        self.attribute_gene.decorate(self.mock_organism)

    def test_attributes_given_to_organism(self):
        for attribute in self.TestAttributeGene.attributes:
            self.assertTrue(hasattr(self.mock_organism, attribute))

    def test_attributes_set_to_initial_value(self):
        for attribute, value in self.TestAttributeGene.attributes.items():
            self.assertEqual(getattr(self.mock_organism, attribute), value)

    def test_method_attributes_given_to_organism(self):
        self.assertTrue(hasattr(self.mock_organism, 'frobnicate'))

    def test_method_attributes_work(self):
        self.mock_organism.frobnicate()
        self.assertEqual(self.mock_organism.foo, 1)
        self.assertEqual(self.mock_organism.bar, 'the new value of bar')

    @skip
    def test_register_method_attribute_logs(self):
        mock_organism = Mock(spec=Organism)
        self.attribute_gene.decorate(self.mock_organism)
        BaseGene.logger = Mock()
        BaseGene()
        BaseGene.logger.debug.assert_called_with('Adding gene BaseGene')


class TestEnablerGene(unittest.TestCase):
    class TestEnabler(EnablerGene):
        attributes = {
            'foo': 0,
            'bar': 'the initial value of bar',
        }

        def add_behaviour(self):
            def frobnicate(self):
                self.foo += 1
                self.bar = 'the new value of bar'

            self.register_behaviour('frobnicate', frobnicate)

    def setUp(self):
        self.mock_organism = Mock(spec=Organism)
        self.enabler = self.TestEnabler()
        self.enabler.decorate(self.mock_organism)
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
        self.assertTrue(hasattr(self.mock_organism, 'frobnicate'))

    def test_behaviour_works(self):
        self.mock_organism.frobnicate()
        self.assertEqual(self.mock_organism.foo, 1)
        self.assertEqual(self.mock_organism.bar, 'the new value of bar')

    def test_base_enabler_behaviour_method_raises_exception(self):
        expected_message = "EnablerGene.behaviour() method has not been overridden by subclass"
        with self.assertRaises(BehaviourNotImplemented) as context_manager:
            EnablerGene()
        self.assertEqual(context_manager.exception.message, expected_message)

    def test_maximum_1_behaviour(self):
        def bar(self):
            pass

        with self.assertRaises(TooManyBehaviours) as context_manager:
            self.enabler.register_behaviour('bar', bar)

        self.assertEqual(context_manager.exception.message, "Multiple behaviours from one gene not supported")

    def test_get_all_genes_on_base_returns_enablers(self):
        self.assertIn(self.enabler, BaseGene.get_all_genes())
        self.assertIn(self.non_enabler, BaseGene.get_all_genes())

    def test_get_all_genes_on_enabler_returns_only_enablers(self):
        self.assertIn(self.enabler, EnablerGene.get_all_genes())
        self.assertNotIn(self.non_enabler, EnablerGene.get_all_genes())


if __name__ == '__main__':
    unittest.main()
