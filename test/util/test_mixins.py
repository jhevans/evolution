from unittest.mock import patch, Mock

from util.mixins import LoggerMixin


__author__ = 'John H Evans'

import unittest


class TestLoggerMixin(unittest.TestCase):
    @patch('logging.getLogger')
    def test_get_logger(self, mock_getLogger):
        LoggerMixin().get_logger()
        mock_getLogger.assert_called_with('evolution.util.mixins.LoggerMixin')

    @patch('logging.getLogger')
    def test_debug(self, mock_getLogger):
        mock_logger = Mock()
        mock_getLogger.return_value = mock_logger
        LoggerMixin().debug('foo')
        mock_logger.debug.assert_called_with('foo')

    @patch('logging.getLogger')
    def test_info(self, mock_getLogger):
        mock_logger = Mock()
        mock_getLogger.return_value = mock_logger
        LoggerMixin().info('foo')
        mock_logger.info.assert_called_with('foo')

    @patch('logging.getLogger')
    def test_warning(self, mock_getLogger):
        mock_logger = Mock()
        mock_getLogger.return_value = mock_logger
        LoggerMixin().warning('foo')
        mock_logger.warning.assert_called_with('foo')

    @patch('logging.getLogger')
    def test_error(self, mock_getLogger):
        mock_logger = Mock()
        mock_getLogger.return_value = mock_logger
        LoggerMixin().error('foo')
        mock_logger.error.assert_called_with('foo')

    @patch('logging.getLogger')
    def test_critical(self, mock_getLogger):
        mock_logger = Mock()
        mock_getLogger.return_value = mock_logger
        LoggerMixin().critical('foo')
        mock_logger.critical.assert_called_with('foo')


if __name__ == '__main__':
    unittest.main()
