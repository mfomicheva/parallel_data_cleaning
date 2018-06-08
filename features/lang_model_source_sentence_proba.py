from features.base_feature import LanguageModelFeature


class LangModelSourceSentenceProba(LanguageModelFeature):

    name = 'lang_model_source_sentence_proba'

    def __init__(self, source, target):
        super().__init__(source, target)

    def run(self):
        self.score = self._lang_model_score(self.src)
