import langid

from parallel_data_cleaning.complex_features_abstract import ComplexFeature
from parallel_data_cleaning.complex_features_abstract import LanguageModel
from parallel_data_cleaning.complex_features_abstract import LexicalProbability


class Langid(ComplexFeature):

    def score(self, input_data, lang=None, **kwargs):
        pred_lang = langid.classify(input_data.source_or_target)
        return int(pred_lang[0] == lang)


class Embeddings(ComplexFeature):

    def __init__(self, resources=None):
        super(Embeddings, self).__init__()
        self.model = dict()
        self.model['source'] = resources['source'].loaded['embeddings']
        self.model['target'] = resources['target'].loaded['embeddings']

    def score(self, input_data, segid=None):
        source_embedding = self.model['source'][segid]
        target_embedding = self.model['target'][segid]
        return source_embedding.dot(target_embedding)


class LanguageModelProbability(LanguageModel):

    def score(self, input_data, **kwargs):
        return self.model.score(input_data.source_or_target)


class LanguageModelPerplexity(LanguageModel):

    def score(self, input_data, **kwargs):
        return self.model.perplexity(input_data.source_or_target)

    
class LexicalProbabilityDirect(LexicalProbability):

    def score(self, input_data, **kwargs):
        return self._score_ibm1_vit_avg(input_data.source, input_data.target)


class LexicalProbabilityInverse(LexicalProbability):

    def score(self, input_data, **kwargs):
        return self._score_ibm1_vit_avg(input_data.target, input_data.source)

    
class LexicalCrossEntropyDirect(LexicalProbability):

    def score(self, input_data, **kwargs):
        return self._xent(input_data.source, input_data.target)


class LexicalCrossEntropyInverse(LexicalProbability):

    def score(self, input_data, **kwargs):
        return self._xent(input_data.target, input_data.source)
