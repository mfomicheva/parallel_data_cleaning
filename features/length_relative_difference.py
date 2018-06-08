from features.base_feature import LengthFeature


class LengthRelativeDifference(LengthFeature):

    name = 'length_relative_difference'

    def __init__(self, source, target):
        super().__init__(source, target)

    def run(self):
        self.score = self._zero_safe_division(abs(self.src_len() - self.tgt_len()),
            max(self.src_len(), self.tgt_len())
        )
