import kenlm


class Resources(dict):

    def __init__(self):
        super().__init__()
        self['language_model'] = dict()
        self['lexical_table'] = dict()

    def load_resources(self, config):
        self['language_model']['source'] = kenlm.Model(config['source_language_model'])
        self['language_model']['target'] = kenlm.Model(config['target_language_model'])
        self['lexical_table']['source'] = self._load_table(config['source_lexical_table'])
        self['lexical_table']['target'] = self._load_table(config['target_lexical_table'])

    @staticmethod
    def _load_table(path):
        table = {}
        for line in open(path):
            parts = line.strip().split()
            table[parts[0], parts[1]] = parts[2]
        return table
