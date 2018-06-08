import kenlm


class LanguageResources:

    def __init__(self, config):
        self.src_lm = self._load_lm(config.source_lang_model)
        self.tgt_lm = self._load_lm(config.target_lang_model)
        # TODO: add lexical tables

    @staticmethod
    def _load_lm(path):
        return kenlm.Model(path)
