

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

    def _score_ibm1_vit_avg(self, s1, s2):
        # computes p(s1 | s2) via viterbi Ibm1 model
        s2_words = set(s2)
        score = 1.
        for w1 in s1:
            #options = [(10**-7, 'NULL')] + [(self.model[w1, w], w) for w in s2_words]
            #w_score, w2 = max(options) # get max alignment word in s2
            options = [10**-7] + [self.model[w1, w] for w in s2_words]
            score *= max(options)
        score = score**(1./len(s1))
        return score


    
class LexicalProbabilityDirect(LexicalProbability):

    def score(self, input_data):
        return self._score_ibm1_vit_avg(input_data.source, input_data.target)


class LexicalProbabilityInverse(LexicalProbability):

    def score(self, input_data):
        return self._score_ibm1_vit_avg(input_data.target, input_data.source)