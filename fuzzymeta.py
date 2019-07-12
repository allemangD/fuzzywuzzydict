from fuzzywuzzy import process


class fuzzydict(dict):
    score_cutoff = 80

    def get(self, item, default=None):
        try:
            return self[item]
        except KeyError:
            return default

    def get_many(self, item):
        if not self:
            return

        for value, _, _ in process.extractBests(item, self, score_cutoff=self.score_cutoff):
            yield value

    def __getitem__(self, item):
        if not self:
            raise KeyError('fuzzydict is empty')

        try:
            value, _, _ = process.extractOne(item, self, score_cutoff=self.score_cutoff)
            return value
        except TypeError:
            pass

        return super().__getitem__(item)

    def __contains__(self, item):
        if not self:
            return False

        try:
            _ = self[item]
            return True
        except KeyError:
            return False


class fuzzyobject:
    __score_cutoff = 50

    def __getattr__(self, item):
        try:
            item, _ = process.extractOne(item, dir(self), score_cutoff=self.__score_cutoff)
        except TypeError:
            pass

        return super(fuzzyobject, self).__getattribute__(item)

    def __setattr__(self, item, value):
        try:
            item, _ = process.extractOne(item, dir(self), score_cutoff=self.__score_cutoff)
        except TypeError:
            pass

        super(fuzzyobject, self).__setattr__(item, value)


class fuzzymeta(fuzzyobject, type):
    def __new__(mcs, name, bases, dct):
        return super().__new__(mcs, name, bases + (fuzzyobject,), dct)
