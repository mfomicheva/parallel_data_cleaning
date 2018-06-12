

class LanguageModel:

    def __init__(self, preloaded_models):
        self.model = preloaded_models.loaded['language_model']


class LanguageModelProbability(LanguageModel):

    def score(self, sentence):
        return self.model.score(sentence)


class LanguageModelPerplexity(LanguageModel):

    def score(self, sentence):
        return self.model.perplexity(sentence)


class LexicalProbability:

    def __init__(self, preloaded_models):
        self.model = preloaded_models.loaded['lexical_table']

    def score(self, sentence):
        return 0.
