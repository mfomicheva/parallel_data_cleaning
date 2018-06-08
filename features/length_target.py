from features.base_feature import LengthFeature


class LengthTarget(LengthFeature):

    name = 'length_target'

    def run(self):
        self.score = self.tgt_len()
