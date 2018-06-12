import complex_features
from patterns import Patterns
from units import Units


class Feature:

    def __init__(self):
        self.name = None
        self.feature_type = None
        self.applies_to = None
        self.feature_class = None
        self.units = None
        self.logic = None


class FeatureExecutor:

    def __init__(self, source, target, feature, resources):
        self.source = source
        self.target = target
        self.feature = feature
        self.resources = resources
        self.patterns = Patterns()
        self.units = Units()

    def _get_input_pair(self, units):
        return self.units.get_units(self.source, units), self.units.get_units(self.target, units)

    @staticmethod
    def _concatenate(*args):
        return '_'.join(args)


class SimpleFeatureExecutor(FeatureExecutor):

    def run(self):
        results = {}
        for pattern in self.feature.logic:
            for unit_type in self.feature.units:
                input_pair = self._get_input_pair(unit_type)
                if not self.feature.applies_to:
                    feature_name = self._concatenate(self.feature.name, pattern, unit_type)
                    results.update({feature_name: self._run_pattern(input_pair, pattern)})
                else:
                    for i, side in enumerate(self.feature.applies_to):
                        feature_name = self._concatenate(self.feature.name, pattern, unit_type, side)
                        results.update({feature_name: self._run_pattern(input_pair[i], pattern)})
        return results

    def _run_pattern(self, input_, pattern):
        return getattr(self.patterns, pattern)(input_)


class ComplexFeatureExecutor(FeatureExecutor):

    def run(self):
        results = {}
        for unit_type in self.feature.units:
            input_pair = self._get_input_pair(unit_type)
            if not self.feature.applies_to:
                feature_class = self._load_complex_feature_class(self.feature.feature_class, self.resources)
                feature_name = self._concatenate(self.feature.name, unit_type)
                results.update({feature_name: feature_class.score(input_pair)})
            else:
                for i, side in enumerate(self.feature.applies_to):
                    feature_class = self._load_complex_feature_class(self.feature.feature_class, self.resources[side])
                    feature_name = self._concatenate(self.feature.name, unit_type, side)
                    results.update({feature_name: feature_class.score(input_pair[i])})
        return results

    @staticmethod
    def _load_complex_feature_class(name, resources):
        return getattr(complex_features, name)(resources)
