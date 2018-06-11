

class Patterns:

    @staticmethod
    def count(input):
        return len(input)

    @staticmethod
    def ratio(input):
        return len(input[0]) / len(input[1]) if len(input[1]) else 0

    @staticmethod
    def inverse_ratio(input):
        return len(input[1]) / len(input[0]) if len(input[0]) else 0

    @staticmethod
    def difference(input):
        return abs(len(input[0]) - len(input[1]))

    def difference_normalized(self, input):
        return self._zero_safe(self.difference(input), self._maximum_length(input))

    def jaccard_index(self, input):
        set1 = set(input[0])
        set2 = set(input[1])
        return self._zero_safe(len(set1.intersection(set2)), len(set1.union(set2)))

    @staticmethod
    def _zero_safe(a, b):
        return a / b if b else 0.

    @staticmethod
    def _maximum_length(input):
        return max(len(input[0]), len(input[1]))
