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

    def _get_input(self, units):
        return self.units.get_units(self.source, units), self.units.get_units(self.target, units)

    @staticmethod
    def _concatenate(*args):
        return '_'.join(args)


class SimpleFeatureExecutor(FeatureExecutor):

    def run(self):
        results = {}
        for pattern in self.feature.logic:
            for unit in self.feature.units:
                input = self._get_input(unit)
                if not self.feature.applies_to:
                    feature_name = self._concatenate(self.feature.name, pattern, unit)
                    results.update({feature_name: self._run_pattern(input, pattern)})
                else:
                    for i, side in enumerate(self.feature.applies_to):
                        feature_name = self._concatenate(self.feature.name, pattern, unit, side)
                        results.update({feature_name: self._run_pattern(input[i], pattern)})
        return results

    def _run_pattern(self, input, pattern):
        return getattr(self.patterns, pattern)(input)


class ComplexFeatureExecutor(FeatureExecutor):

    def run(self):
        results = {}
        for unit in self.feature.units:
            input = self._get_input(unit)
            if not self.feature.applies_to:
                feature_class = self._load_complex_feature_class(self.feature.feature_class, self.resources)
                feature_name = self._concatenate(self.feature.name, unit)
                results.update({feature_name: feature_class.score(input, side=None)})
            else:
                for i, side in enumerate(self.feature.applies_to):
                    feature_class = self._load_complex_feature_class(self.feature.feature_class, self.resources[side])
                    feature_name = self._concatenate(self.feature.name, unit, side)
                    results.update({feature_name: feature_class.score(input[i])})
        return results

    @staticmethod
    def _load_complex_feature_class(name, resources):
        return getattr(complex_features, name)(resources)


class FeatureExecutor:

    def __init__(self, source, target, features, resources):
        self.source = source
        self.target = target
        self.resources = resources
        self.features = features
        self.patterns = Patterns()
        self.units = Units()

    def execute(self):
        results = {}
        for feature in self.features:
            if feature.feature_type == 'simple':
                results.update(self._run_simple_features(feature))
            else:
                results.update(self._run_complex_feature(feature))
        return results

    def _run_simple_features(self, feature):
        results = {}
        for pattern in feature.logic:
            for unit in feature.units:
                input = self._get_input(unit)
                if not feature.applies_to:
                    feature_name = self._concatenate(feature.name, pattern, unit)
                    results.update({feature_name: self._run_simple_feature(input, pattern)})
                else:
                    for i, side in enumerate(feature.applies_to):
                        feature_name = self._concatenate(feature.name, pattern, unit, side)
                        results.update({feature_name: self._run_simple_feature(input[i], pattern)})
        return results

    def _run_complex_feature(self, feature):
        results = {}
        for unit in feature.units:
            input = self._get_input(unit)
            if not feature.applies_to:
                feature_class = self._load_complex_feature_class(feature.feature_class, self.resources)
                feature_name = self._concatenate(feature.name, unit)
                results.update({feature_name: feature_class.score(input, side=None)})
            else:
                for i, side in enumerate(feature.applies_to):
                    feature_class = self._load_complex_feature_class(feature.feature_class, self.resources[side])
                    feature_name = self._concatenate(feature.name, unit, side)
                    results.update({feature_name: feature_class.score(input[i])})
        return results

    def _run_simple_feature(self, input, pattern):
        return getattr(self.patterns, pattern)(input)

    @staticmethod
    def _load_complex_feature_class(name, resources):
        return getattr(complex_features, name)(resources)

    def _get_input(self, units):
        return self.units.get_units(self.source, units), self.units.get_units(self.target, units)

    @staticmethod
    def _concatenate(*args):
        return '_'.join(args)
