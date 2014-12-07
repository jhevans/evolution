import logging

__author__ = 'John H Evans'


class LoggerMixin(object):
    @classmethod
    def get_logger(cls):
        logger_name = 'evolution.' + cls.__module__ + '.' + cls.__name__
        return logging.getLogger(logger_name)

    @classmethod
    def debug(cls, message):
        cls.get_logger().debug(message)

    @classmethod
    def info(cls, message):
        cls.get_logger().info(message)

    @classmethod
    def warning(cls, message):
        cls.get_logger().warning(message)

    @classmethod
    def error(cls, message):
        cls.get_logger().error(message)

    @classmethod
    def critical(cls, message):
        cls.get_logger().critical(message)