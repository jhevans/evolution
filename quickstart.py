from random import random

from genes.pseudo_genes import Mortality, Senescence
from organism.organism import Organism


__author__ = 'John H Evans'


def run():
    genes = [
        Mortality(),
        Senescence(inject__random=random),
    ]

    organisms = []
    for _ in range(20):
        organism = Organism()
        for gene in genes:
            gene.decorate(organism)
        organisms.append(organism)

    for n in range(100):
        dead_count = 0
        print("====================")
        print("age = ", n)
        for organism in organisms:
            organism.increment_age()
            # print(organism.name, organism.alive)
            if not organism.alive:
                dead_count += 1

        print(dead_count, "organisms have died")
        if dead_count == len(organisms):
            break

    for organism in organisms:
        print(organism.name, "died at age", organism.died_age)

    print("Done")


if __name__ == '__main__':
    run()