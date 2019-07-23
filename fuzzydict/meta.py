from fuzzywuzzy import process

__all__ = ['fuzzyobject', 'fuzzymeta']


class fuzzyobject:
    """Similar behavior to fuzzydict, but with attribute access.

    This would be similar to setting __dict__ = fuzzydict(), except that __setattr__
    is defined here.
    """

    __score_cutoff = 50

    def __getattr__(self, item):
        try:
            item, _ = process.extractOne(item, dir(self),
                                         score_cutoff=self.__score_cutoff)
        except TypeError:
            pass

        return super(fuzzyobject, self).__getattribute__(item)

    def __setattr__(self, item, value):
        try:
            item, _ = process.extractOne(item, dir(self),
                                         score_cutoff=self.__score_cutoff)
        except TypeError:
            pass

        super(fuzzyobject, self).__setattr__(item, value)


class fuzzymeta(fuzzyobject, type):
    """Similar behavior to fuzzyobject, but on the class; this way class attribute
    lookup is also fuzzy.

    Instances of classes with this metaclass automatically inherit from fuzzyobject.
    """

    def __new__(mcs, name, bases, dct):
        return super().__new__(mcs, name, bases + (fuzzyobject,), dct)
