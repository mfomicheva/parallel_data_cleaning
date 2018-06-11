import complex_features
from patterns import Patterns
from units import Units


class FeatureExecutor:

    def __init__(self, source, target, config, resources):
        self.source = source
        self.target = target
        self.resources = resources
        self.features = config['features']
        self.patterns = Patterns()
        self.units = Units()

    def execute(self):
        results = {}
        for feature in self.features:
            if feature['type'] == 'simple':
                results.update(self._run_simple_features(feature))
            else:
                results.update(self._run_complex_feature(feature))
        return results

    def _run_simple_features(self, feature):
        units = feature['units']
        sides = feature['applies_to']
        feature_patterns = feature['logic']
        results = {}
        for pattern in feature_patterns:
            for unit in units:
                input = self._get_input(unit)
                if not sides:
                    feature_name = self._concatenate(feature['name'], pattern, unit)
                    results.update({feature_name: self._run_simple_feature(input, pattern)})
                else:
                    for i, side in enumerate(sides):
                        feature_name = self._concatenate(feature['name'], pattern, unit, side)
                        results.update({feature_name: self._run_simple_feature(input[i], pattern)})
        return results

    def _run_complex_feature(self, feature):
        results = {}
        sides = feature['applies_to']
        feature_class = self._load_complex_feature_class(feature['class'], self.resources)
        for unit in feature['units']:
            input = self._get_input(unit)
            if not sides:
                feature_name = self._concatenate(feature['name'], unit)
                results.update({feature_name: feature_class.score(input, side=None)})
            else:
                for i, side in enumerate(sides):
                    feature_name = self._concatenate(feature['name'], unit, side)
                    results.update({feature_name: feature_class.score(input[i], side=side)})
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
