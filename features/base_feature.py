

class BaseFeature:

    name = None

    def __init__(self, source, target, resources):
        self.src = source
        self.tgt = target
        self.resources = resources
        self.score = None

    def src_len(self):
        return len(self._list(self.src))

    def tgt_len(self):
        return len(self._list(self.tgt))

    @staticmethod
    def _list(line):
        return line.strip().split()

    @staticmethod
    def _zero_safe_division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 0.


class LengthFeature(BaseFeature):
    pass


class LanguageModelFeature(BaseFeature):

    def _lang_model_score(self, line):
        return self.resources.src_lm.score(line, bos=True, eos=True)


class MismatchFeature(BaseFeature):

    @staticmethod
    def _is_number(token):
        return all(char.isdigit() for char in token)

    @staticmethod
    def _is_alphanum(token):
        pass


class AlignmentFeature(BaseFeature):
    pass