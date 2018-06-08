from features.lang_model_source_sentence_proba import LangModelSourceSentenceProba


class LangModelSourceSentencePerpl(LangModelSourceSentenceProba):

    name = 'lang_model_source_sentence_perp'

    def run(self):
        self.score = self._lang_model_score(self.src)

    def _lang_model_score(self, line):
        return self.resources.src_lm.perplexity(line)
