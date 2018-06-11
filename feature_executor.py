import sys

from string import punctuation


class FeatureExecutor:

    def __init__(self, source, target, config, resources):
        self.source = source
        self.target = target
        self.resources = resources
        self.config = config

    def execute(self):
        results = {}
        for feature in self.config['features']:
            if feature['type'] == 'simple':
                results.update(self._run_simple_feature(feature))
            else:
                if 'resource' in feature:
                    results.update(self._run_resource_feature(feature))
        return results

    def _run_resource_feature(self, feature):
        results = {}
        side = feature['applies_to']
        model = self.resources[feature['resource']]
        for unit in feature['units']:
            input = self._get_input(unit)
            feature_name = self._feature_name(feature['name'], feature['applies_to'], unit)
            results.update({feature_name: eval(feature['logic'])})
        return results

    def _run_simple_feature(self, feature):
        results = {}
        for unit in feature['units']:
            input = self._get_input(unit)
            feature_name = self._feature_name(feature['name'], feature['applies_to'], unit)
            results.update({feature_name: self._run_feature(feature, input)})
        return results

    def _get_input(self, units):
        return self._get_units(self.source, units), self._get_units(self.target, units)

    def _get_units(self, initial_input, unit):
        if unit == 'sentence':
            return initial_input.strip()
        elif unit == 'words':
            return initial_input.strip().split()
        elif unit == 'numbers':
            return self._get_numbers(initial_input.strip().split())
        elif unit == 'alphanums':
            return self._get_alphanums(initial_input.strip().split())
        elif unit in '.,:;!?':
            return self._get_punct_mark(initial_input.strip().split(), unit)
        elif unit == 'punctuation':
            return self._get_punct_marks(initial_input.strip().split())
        else:
            sys.stderr.write('Error! Invalid unit type {}\n'.format(unit))

    @staticmethod
    def _get_punct_marks(tokens):
        result = []
        for token in tokens:
            if token in punctuation:
                result.append(token)
        return result

    @staticmethod
    def _get_punct_mark(tokens, mark):
        result = []
        for token in tokens:
            if token == mark:
                result.append(token)
        return result

    @staticmethod
    def _get_numbers(tokens):
        result = []
        for token in tokens:
            if all(char.isdigit() for char in token):
                result.append(token)
        return result

    @staticmethod
    def _get_alphanums(tokens):
        result = []
        for token in tokens:
            token = token.replace('-', '')
            if not token.isalpha():
                result.append(token)
        return result

    @staticmethod
    def _feature_name(name, applies_to, unit):
        if applies_to in ('source', 'target'):
            return '{}_{}_{}'.format(name, applies_to, unit)
        else:
            return '{}_{}'.format(name, unit)

    @staticmethod
    def _run_feature(feature, input):
        return eval(feature['logic'])
