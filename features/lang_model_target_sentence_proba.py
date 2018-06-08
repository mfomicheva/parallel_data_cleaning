from features.base_feature import LanguageModelFeature


class LangModelTargetSentenceProba(LanguageModelFeature):

    name = 'lang_model_target_sentence_proba'

    def run(self):
        self.score = self._lang_model_score(self.tgt)
