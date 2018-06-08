from load_resources import load_lm
from parse_args import args


class BaseFeature:

    name = None

    def __init__(self, source, target):
        self.src = source
        self.tgt = target
        self.score = None

    def src_len(self):
        return len(self._list(self.src))

    def tgt_len(self):
        return len(self._list(self.tgt))

    @staticmethod
    def _list(line):
        return line.strip().split()


class LengthFeature(BaseFeature):
    pass


class LanguageModelFeature(BaseFeature):

    model = load_lm(args.source_lang_model)

    def _lang_model_score(self, line):
        return self.model.score(line, bos=True, eos=True)


class MismatchFeature(BaseFeature):

    @staticmethod
    def _is_number(token):
        return all(char.isdigit() for char in token)

    @staticmethod
    def _is_alphanum(token):
        pass


class AlignmentFeature(BaseFeature):
    pass