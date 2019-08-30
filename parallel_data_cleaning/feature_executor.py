import sys

from parallel_data_cleaning import complex_features
from parallel_data_cleaning.patterns import Patterns
from parallel_data_cleaning.input_data import InputData


class Feature:

    def __init__(self):
        self.name = None
        self.feature_type = None
        self.applies_to = None
        self.feature_class = None
        self.units = None
        self.logic = None


class FeatureExecutor:

    def __init__(self, segid, source, target, feature, resources):
        self.segid = segid
        self.source = source
        self.target = target
        self.feature = feature
        self.resources = resources
        self.patterns = Patterns()

    @staticmethod
    def _concatenate(*args):
        return '_'.join(args)

    def _side_by_name(self, side_name):
        if side_name == 'source':
            return self.source
        elif side_name == 'target':
            return self.target
        else:
            sys.stderr.write('applies_to is invalid, should be source or target'.format(side_name))
            sys.exit()


class SimpleFeatureExecutor(FeatureExecutor):

    def run(self):
        results = {}
        for unit_type in self.feature.units:
            input_data = InputData()
            input_data.get_input_representation(self.source, self.target, unit_type)
            for pattern in self.feature.logic:
                if not self.feature.applies_to:
                    feature_name = self._concatenate(self.feature.name, pattern, unit_type)
                    results.update({feature_name: self._run_pattern(input_data, pattern)})
                else:
                    for side in self.feature.applies_to:
                        input_data.set_source_or_target(self._side_by_name(side), unit_type)
                        feature_name = self._concatenate(self.feature.name, pattern, unit_type, side)
                        results.update({feature_name: self._run_pattern(input_data, pattern)})
        return results

    def _run_pattern(self, input_data, pattern):
        return getattr(self.patterns, pattern)(input_data)


class ComplexFeatureExecutor(FeatureExecutor):

    def run(self):
        results = {}
        for unit_type in self.feature.units:
            input_data = InputData()
            input_data.get_input_representation(self.source, self.target, unit_type)
            if not self.feature.applies_to:
                feature_class = self._load_complex_feature_class(self.feature.feature_class, self.resources)
                feature_name = self._concatenate(self.feature.name, unit_type)
                results.update({feature_name: feature_class.score(input_data, segid=self.segid)})
            else:
                for side in self.feature.applies_to:
                    feature_class = self._load_complex_feature_class(self.feature.feature_class, self.resources[side])
                    input_data.set_source_or_target(self._side_by_name(side), unit_type)
                    feature_name = self._concatenate(self.feature.name, unit_type, side)
                    results.update({feature_name: feature_class.score(input_data, segid=self.segid)})
        return results

    @staticmethod
    def _load_complex_feature_class(feature_name, resources):
        return getattr(complex_features, feature_name)(resources)
