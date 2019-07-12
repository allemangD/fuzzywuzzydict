from fuzzywuzzy import process


class fuzzydict(dict):
    score_cutoff = 0

    def get(self, item, default=None):
        try:
            return self[item]
        except KeyError:
            return default

    def get_many(self, item):
        for k, r in process.extract(item, self.keys()):
            if r < self.score_cutoff:
                continue

            yield dict.get(self, k)

    def __getitem__(self, item):
        if not self:
            raise KeyError('fuzzydict is empty')

        k, r = process.extractOne(item, self.keys())

        if r < self.score_cutoff:
            raise KeyError('No key matches item above threshold')

        return dict.get(self, k)

    def __contains__(self, item):
        try:
            if self:
                e = self[item]
                return True
        except KeyError:
            pass

        return False


class fuzzyobject:
    __score_cutoff = 50

    def __getattr__(self, item):
        try:
            k, v = process.extractOne(item, dir(self), score_cutoff=self.__score_cutoff)
            return getattr(self, k)
        except TypeError:
            pass

        raise AttributeError('Cannot fuzzy-match given attribute.')


class fuzzymeta(fuzzyobject, type):
    def __new__(mcs, name, bases, dct):
        return super().__new__(mcs, name, bases + (fuzzyobject,), dct)
