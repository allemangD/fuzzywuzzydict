from fuzzywuzzy import process

__all__ = ['fuzzydict']


class fuzzydict(dict):
    """Use fuzzywuzzy to get the value of the closest matching key

    On __getitem__ and __contains__, use fuzzywuzzy.process to rank the keys and choose
    whichever matches best. If no keys match above the threshold, consider the key to
    not be in the map.
    """

    score_cutoff = 80

    def get(self, item, default=None):
        try:
            return self[item]
        except KeyError:
            return default

    def get_many(self, item):
        if not self:
            return

        for value, _, _ in process.extractBests(
                item, self, score_cutoff=self.score_cutoff):
            yield value

    def __getitem__(self, item):
        if not self:
            raise KeyError('fuzzydict is empty')

        try:
            value, _, _ = process.extractOne(
                item, self, score_cutoff=self.score_cutoff)
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
