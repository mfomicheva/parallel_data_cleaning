from features.base_feature import LengthFeature


class LengthAbsoluteDifference(LengthFeature):

    name = 'length_absolute_difference'

    def run(self):
        self.score = abs(self.src_len() - self.tgt_len())
