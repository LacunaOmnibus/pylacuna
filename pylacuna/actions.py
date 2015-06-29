#!/usr/bin/env python

import building

class Actions(set):
    '''
    MIDDLEWARE.

    Methods for dealing with Actions.

    The idea behind this is to have a class that encapsulates player actions
    (i.e. the subset of api calls that have to do with actually playing the
    game)

    An action might a building upgrade. So maybe a ref to a building object
    and the name of the method and arguments to call. We can use functools.partial
    to accomplish this.
    from functools import partial
    b = Building(initial_dict)
    action = Actions([partial(b.upgrade)])
    '''
    def __init__(self, actions):
        super(Action, self).__init__(actions)

