from features.base_feature import LengthFeature


class LengthTargetSourceRatio(LengthFeature):

    name = 'length_target_source_ratio'

    def run(self):
        self.score = self._zero_safe_division(self.src_len(), self.tgt_len())
