import kenlm


class Resources:

    def __init__(self):
        self.paths = dict()
        self.loaded = dict()

    def load_resources(self):
        self.loaded['language_model'] = kenlm.Model(self.paths['language_model'])
        self.loaded['lexical_table'] = self._load_table(self.paths['lexical_table'])

    @staticmethod
    def _load_table(path):
        table = {}
        for line in open(path):
            parts = line.strip().split()
            table[parts[0], parts[1]] = parts[2]
        return table
