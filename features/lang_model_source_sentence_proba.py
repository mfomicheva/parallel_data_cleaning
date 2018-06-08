from features.base_feature import LanguageModelFeature


class LangModelSourceSentenceProba(LanguageModelFeature):

    name = 'lang_model_source_sentence_proba'

    def run(self):
        self.score = self._lang_model_score(self.src)
