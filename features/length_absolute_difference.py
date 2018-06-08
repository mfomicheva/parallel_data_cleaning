from features.base_feature import LengthFeature


class LengthAbsoluteDifference(LengthFeature):

    name = 'length_absolute_difference'

    def __init__(self, source, target):
        super().__init__(source, target)

    def run(self):
        self.score = abs(self.src_len() - self.tgt_len())
