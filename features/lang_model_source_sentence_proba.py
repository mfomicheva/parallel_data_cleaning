from features.base_feature import LanguageModelFeature
from load_resources import load_lm
from parse_args import args


class LangModelSourceSentenceProba(LanguageModelFeature):

    name = 'lang_model_source_sentence_proba'
    model = load_lm(args.source_lang_model)

    def __init__(self, source, target):
        super().__init__(source, target)

    def run(self):
        self.score = self.model.score(self.src, bos=True, eos=True)
