

class LanguageModel:

    def __init__(self, preloaded_models):
        self.model = preloaded_models.loaded['language_model']


class LanguageModelProbability(LanguageModel):

    def score(self, input_data):
        return self.model.score(input_data.source_or_target)


class LanguageModelPerplexity(LanguageModel):

    def score(self, input_data):
        return self.model.perplexity(input_data.source_or_target)


class LexicalProbability:

    def __init__(self, preloaded_models):
        self.model = preloaded_models.loaded['lexical_table']

    def score(self, input_data):
        return 0.
