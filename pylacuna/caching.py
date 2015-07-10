#!/usr/bin/env python
'''
Import this module to have access to a global redis cache named GLOBAL_CACHE.

USAGE:
    from caching import GLOBAL_CACHE

    GLOBAL_CACHE.store('foo', 'bar')
    GLOBAL_CACHE.get('foo')
    >> bar
'''

from redis_cache import SimpleCache

try:
    GLOBAL_CACHE
except NameError:
    GLOBAL_CACHE = SimpleCache(limit=1000, expire=60*60*24, namespace="GLOBAL_CACHE")
else:
    # Already defined...
    pass
