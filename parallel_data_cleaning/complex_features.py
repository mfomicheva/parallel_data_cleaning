from math import log


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

    null_word_proba = 10 ** -7
    zero_safe_xent = 10 ** -4

    def __init__(self, preloaded_models):
        self.model = preloaded_models.loaded['lexical_table']

    def _score_ibm1_vit_avg(self, s1, s2):
        # computes p(s1 | s2) via viterbi Ibm1 model
        s2_words = set(s2)
        score = 1.
        for w1 in s1:
            options = [self.null_word_proba] + [self.model[w1][w] for w in s2_words if w1 in self.model and w in self.model[w1]]
            score *= max(options)
        score **= (1. / len(s1))
        return score

    def _xent(self, s1, s2):
        # original distributions
        vs1 = dict((w, s1.count(w) / len(s1)) for w in s1)
        vs2 = dict((w, s2.count(w) / len(s2)) for w in s2)

        # compute translation
        vps1 = dict()
        for w1 in vs1.keys():
            score = sum(vs2[w2] * self.model[w1][w2] for w2 in vs2 if w1 in self.model and w2 in self.model[w1])
            if score == 0 and w1 in s2:
                score = 1.  # word not in vocabulary, assume copied
            vps1[w1] = score
        xent = sum(vs1[w] * log(1. / (vps1[w] + self.zero_safe_xent)) for w in vs1)
        return xent

    
class LexicalProbabilityDirect(LexicalProbability):

    def score(self, input_data):
        return self._score_ibm1_vit_avg(input_data.source, input_data.target)


class LexicalProbabilityInverse(LexicalProbability):

    def score(self, input_data):
        return self._score_ibm1_vit_avg(input_data.target, input_data.source)

    
class LexicalCrossEntropyDirect(LexicalProbability):

    def score(self, input_data):
        return self._xent(input_data.source, input_data.target)


class LexicalCrossEntropyInverse(LexicalProbability):

    def score(self, input_data):
        return self._xent(input_data.target, input_data.source)
