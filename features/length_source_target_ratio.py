from features.base_feature import LengthFeature
from features.utils import zero_safe_division


class LengthSourceTargetRatio(LengthFeature):

    name = 'length_source_target_ratio'

    def __init__(self, source, target):
        super().__init__(source, target)

    def run(self):
        self.score = zero_safe_division(self.src_len(), self.tgt_len())