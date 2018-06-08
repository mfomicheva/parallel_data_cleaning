from features.lang_model_target_sentence_proba import LangModelTargetSentenceProba


class LangModelTargetSentencePerpl(LangModelTargetSentenceProba):

    def _lang_model_score(self, line):
        return self.resources.tgt_lm.perplexity(line)
