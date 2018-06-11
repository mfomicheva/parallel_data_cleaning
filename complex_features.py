

class LanguageModel:

    def __init__(self, preloaded_models):
        self.preloaded_models = preloaded_models['language_model']


class LanguageModelProbability(LanguageModel):

    def score(self, input, side):
        return self.preloaded_models[side].score(input)


class LanguageModelPerplexity(LanguageModel):

    def score(self, input, side):
        return self.preloaded_models[side].perplexity(input)


class LexicalProbability:

    def __init__(self, preloaded_models):
        self.preloaded_models = preloaded_models['lexical_table']

    def score(self, input, side):
        return 0.


class LexicalMatches:

    def __init__(self):
        pass

    def score(self, input):
        pass

    def _compute_matches(self):
        pass
