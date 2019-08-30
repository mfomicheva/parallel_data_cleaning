

class Patterns:

    @staticmethod
    def count(input_data):
        return len(input_data.source_or_target)

    @staticmethod
    def ratio(input_data):
        return len(input_data.source) / len(input_data.target) if len(input_data.target) else 0

    @staticmethod
    def inverse_ratio(input_data):
        return len(input_data.target) / len(input_data.source) if len(input_data.source) else 0

    def jaccard_index(self, input_data):
        set1 = set(input_data.source)
        set2 = set(input_data.target)
        return self._zero_safe(len(set1.intersection(set2)), len(set1.union(set2)))

    def difference_normalized(self, input_data):
        return self._zero_safe(self.difference(input_data), self._maximum_length(input_data))

    @staticmethod
    def difference(input_data):
        return abs(len(input_data.source) - len(input_data.target))

    @staticmethod
    def _zero_safe(a, b):
        return a / b if b else 0.

    @staticmethod
    def _maximum_length(input_data):
        return max(len(input_data.source), len(input_data.target))
