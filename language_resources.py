import kenlm


class LanguageModel(dict):

    def __init__(self, config):
        super().__init__()
        self['source'] = _load_lm(config['source_lang_model'])
        self['target'] = _load_lm(config['target_lang_model'])

    def score(self, input, side):
        return self[side].score(input)

    def perplexity(self, input, side):
        return self[side].perplexity(input)


def load_language_resources(config):
    return {
        'language_model': LanguageModel(config)
    }


def _load_lm(path):
    return kenlm.Model(path)
