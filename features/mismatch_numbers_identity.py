from features.base_feature import MismatchFeature


class MismatchNumbersIdentity(MismatchFeature):

    name = 'mismatch_numbers_identity'

    def run(self):
        src_diff = self._missing(self._list(self.src), self._list(self.tgt))
        tgt_diff = self._missing(self._list(self.tgt), self._list(self.src))
        self.score = self._zero_safe_division(
            src_diff + tgt_diff, self.src_len() + self.tgt_len())

    def _missing(self, list1, list2):
        count = 0
        for token in list1:
            if self._is_number(token) and token not in list2:
                count += 1
        return count
