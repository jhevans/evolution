__author__ = 'John H Evans'


class TooManyBehaviours(Exception):
    message = "Multiple behaviours from one gene not supported"


class BehaviourNotImplemented(Exception):
    message = "EnablerGene.behaviour() method has not been overridden by subclass"