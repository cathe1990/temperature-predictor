# _*_ coding: utf-8 _*_

"""
simulators.structures
~~~~~~~~~~~~~~~~~~~~~

Data Structures that power Simulators
"""


class LookupDict(dict):
    """Dictiionary lookup object."""

    def __init__(self, name=None):
        self.name = name
        super(LookupDict, self).__init__()

    def __repr__(self):
        return '<look up {}>'.format(self.name)

    def __getitem__(self, key):
        # fall-throught is allowed here, so values default to None
        return self.__dict__.get(key, None)

    def get(self, key, default=None):
        return self.__dict__.get(key, default)
