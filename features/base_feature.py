

class BaseFeature():

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

    def __init__(self, source, target):
        super().__init__(source, target)


class LanguageModelFeature(BaseFeature):

    def __init__(self, source, target):
        super().__init__(source, target)


class MismatchFeature(BaseFeature):

    def __init__(self, source, target):
        super().__init__(source, target)

    @staticmethod
    def _is_number(token):
        return all(char.isdigit() for char in token)

    @staticmethod
    def _is_alphanum(token):
        pass


class AlignmentFeature(BaseFeature):

    def __init__(self, source, target):
        super().__init__(source, target)
