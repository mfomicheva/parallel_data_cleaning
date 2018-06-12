

class Patterns:

    @staticmethod
    def count(units):
        return len(units)

    @staticmethod
    def ratio(units_pair):
        return len(units_pair[0]) / len(units_pair[1]) if len(units_pair[1]) else 0

    @staticmethod
    def inverse_ratio(units_pair):
        return len(units_pair[1]) / len(units_pair[0]) if len(units_pair[0]) else 0

    def jaccard_index(self, units_pair):
        set1 = set(units_pair[0])
        set2 = set(units_pair[1])
        return self._zero_safe(len(set1.intersection(set2)), len(set1.union(set2)))

    def difference_normalized(self, units_pair):
        return self._zero_safe(self.difference(units_pair), self._maximum_length(units_pair))

    @staticmethod
    def difference(units_pair):
        return abs(len(units_pair[0]) - len(units_pair[1]))

    @staticmethod
    def _zero_safe(a, b):
        return a / b if b else 0.

    @staticmethod
    def _maximum_length(units_pair):
        return max(len(units_pair[0]), len(units_pair[1]))
