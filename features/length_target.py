from features.base_feature import LengthFeature


class LengthTarget(LengthFeature):

    name = 'length_target'

    def __init__(self, source, target):
        super().__init__(source, target)

    def run(self):
        self.score = self.tgt_len()
