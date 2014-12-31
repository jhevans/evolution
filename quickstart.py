import logging
from random import random
import time

from genes.pseudo_genes import Mortality, Senescence
from organism.organism import Organism


__author__ = 'John H Evans'

logging.basicConfig(
    filename='logs/evolution.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(name)s: %(message)s',
    filemode='w',
)


def run():
    print("Instantiating genes...")
    genes = [
        Mortality(),
        Senescence(inject__random=random),
    ]

    print("Creating organisms...")
    organisms = []
    for _ in range(20):
        organism = Organism()
        for gene in genes:
            gene.decorate(organism)
        organisms.append(organism)

    print("Running...")

    start_time = time.time()
    for n in range(1000):
        dead_count = 0
        # print("====================")
        # print("age = ", n)
        for organism in organisms:
            organism.increment_age()
            # print(organism.name, organism.alive)
            if not organism.alive:
                dead_count += 1

        # print(dead_count, "organisms have died")
        if dead_count == len(organisms):
            break

            # for organism in organisms:
            # print(organism.name, "died at age", organism.died_age)

    end_time = time.time()
    print("Done")
    duration = end_time - start_time
    print("Ran for %fs" % duration)


if __name__ == '__main__':
    run()