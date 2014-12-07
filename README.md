evolution
=========

A toy program I've been meaning to create for ages. The idea is to create an evolutionary simulator. Probably easier 
said than done.

The three key concepts are the Gene, the Organism and the Environment.  The Gene is a class which is able to decorate an
Organism, thus granting the Organism abilities or influencing abilities which the Organism may already possess.
An Organism by itself is completely inert, any properties given to an Organism are granted to it by Genes.  The 
environment gives the Organism it's context, relative to other Organisms and to the environment itself.

PseudoGenes are a special class of Genes that give organisms fundamental properties like age, energy and mass.  Unlike 
normal genes they will always be passed on to the next generation through reproduction.  PseudoGene status is given 
using PseudoGeneMixin.

EnablerGenes give organisms behaviours.  Each behaviour will be called at some point when increment_age() is called on 
an organism.  It is up to the behaviour method to decide whether or not to perform an action.  That is if an organism 
has a behaviour move() this function will always be called but will not necessarily result in the organism moving.

TODO:
- Get a very basic environment running with some doomed organisms
- Implement Genesis class for instantiating starting organisms
- Design and implement missing method behaviour of organism
- Implement EnvironmentalContext as class
- Implement supervisor thread to return current state of environment

- Introduce environmental context to organism:
    The organism is only concerned with it's immediate environment.  A gene will need to have some form of limited 
    context in which to operate to stop it becoming overly complicated. The idea is that an organism will receive a 
    context from it's environment. This context will provide some information which genes can use to interact with their 
    environment.
    
    
- Create some enabler genes to get started with
    Photosynthesize - Collect energy from context 'light'
    Reproduce Asexually - Consume energy to create an exact duplicate, mutate occasionally
    Eat - Kill a neighbouring organism and take a part of it's energy
    Move - Consume energy to move to a neighbouring cell
   
- Generate modifier genes
    Enabler genes are intended to be inert on their own, in order for them to have an effect an organism must also have modifiers which give their ability potency.
    Modifiers can potentially be positive or negative and will be generated automatically rather than hard coded.
    