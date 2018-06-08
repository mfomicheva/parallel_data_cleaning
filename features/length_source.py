from features.base_feature import LengthFeature


class LengthSource(LengthFeature):

    name = 'length_source'

    def run(self):
        self.score = self.src_len()
