from features.base_feature import LanguageModelFeature
from load_resources import load_lm
from parse_args import args


class LangModelTargetSentenceProba(LanguageModelFeature):

    name = 'lang_model_target_sentence_proba'
    model = load_lm(args.target_lang_model)

    def run(self):
        self.score = self._lang_model_score(self.tgt)
