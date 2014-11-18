evolution
=========

A toy program I've been meaning to create for ages. The idea is to create an evolutionary simulator. Probably easier said than done.

TODO:
- Introduce environmental context to organism:
    The organism is only concerned with it's immediate environment.  A gene will need to have some form of limited context in which to operate to stop it becoming overly complicated.
    The idea is that an organism will receive a context from it's environment. This context will provide some information which genes can use to interact with their environment.
    
    
- Create some enabler genes to get started with
    Photosynthesize - Collect energy from context 'light'
    Reproduce Asexually - Consume energy to create an exact duplicate, mutate occasionally
    Eat - Kill a neighbouring organism and take a part of it's energy
    Move - Consume energy to move to a neighbouring cell
   
- Generate modifier genes
    Enabler genes are intended to be inert on their own, in order for them to have an effect an organism must also have modifiers which give their ability potency.
    Modifiers can potentially be positive or negative and will be generated automatically rather than hard coded.
    