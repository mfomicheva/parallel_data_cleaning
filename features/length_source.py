from features.base_feature import LengthFeature


class LengthSource(LengthFeature):

    name = 'length_source'

    def __init__(self, source, target):
        super().__init__(source, target)

    def run(self):
        self.score = self.src_len()
