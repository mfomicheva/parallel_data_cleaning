import complex_features
from patterns import Patterns
from input_data import InputData


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

    @staticmethod
    def _concatenate(*args):
        return '_'.join(args)


class SimpleFeatureExecutor(FeatureExecutor):

    def run(self):
        results = {}
        for pattern in self.feature.logic:
            for unit_type in self.feature.units:
                input_data = InputData()
                input_data.get_input_representation(self.source, self.target, unit_type)
                if not self.feature.applies_to:
                    feature_name = self._concatenate(self.feature.name, pattern, unit_type)
                    results.update({feature_name: self._run_pattern(input_data, pattern)})
                else:
                    results.update(self._run_source_or_target(input_data, self.source, pattern, unit_type, 'source'))
                    results.update(self._run_source_or_target(input_data, self.target, pattern, unit_type, 'target'))
        return results

    def _run_pattern(self, input_data, pattern):
        return getattr(self.patterns, pattern)(input_data)

    def _run_source_or_target(self, input_data, source_or_target, pattern, unit_type, side):
        input_data.set_source_or_target(source_or_target, unit_type)
        feature_name = self._concatenate(self.feature.name, pattern, unit_type, side)
        return {feature_name: self._run_pattern(input_data, pattern)}


class ComplexFeatureExecutor(FeatureExecutor):

    def run(self):
        results = {}
        for unit_type in self.feature.units:
            input_data = InputData()
            input_data.get_input_representation(self.source, self.target, unit_type)
            if not self.feature.applies_to:
                feature_class = self._load_complex_feature_class(self.feature.feature_class, self.resources)
                feature_name = self._concatenate(self.feature.name, unit_type)
                results.update({feature_name: feature_class.score(input_data)})
            else:
                self._run_source_or_target(input_data, self.source, unit_type, 'source')
                self._run_source_or_target(input_data, self.target, unit_type, 'target')
        return results

    def _run_source_or_target(self, input_data, source_or_target, unit_type, side):
        feature_class = self._load_complex_feature_class(self.feature.feature_class, self.resources[side])
        input_data.set_source_or_target(source_or_target, unit_type)
        feature_name = self._concatenate(self.feature.name, unit_type, side)
        return {feature_name: feature_class.score(input_data)}

    @staticmethod
    def _load_complex_feature_class(name, resources):
        return getattr(complex_features, name)(resources)
