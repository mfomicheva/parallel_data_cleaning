from features.base_feature import MismatchFeature


class MismatchNumbersCount(MismatchFeature):

    name = 'mismatch_numbers_count'

    def __init__(self, source, target):
        super().__init__(source, target)

    def run(self):
        self.score = abs(self._count(self._list(self.src)) - self._count(self._list(self.tgt)))

    def _count(self, tokens):
        return len([t for t in tokens if self._is_number(t)])
