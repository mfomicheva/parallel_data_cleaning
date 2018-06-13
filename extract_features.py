import yaml
import argparse

from feature_executor import Feature
from feature_executor import SimpleFeatureExecutor
from feature_executor import ComplexFeatureExecutor
from language_resources import Resources


def _get_features(config):
    result = []
    for feature_description in config['features']:
        feature = Feature()
        feature.name = feature_description.get('name', None)
        feature.feature_type = feature_description.get('type', None)
        feature.feature_class = feature_description.get('class', None)
        feature.applies_to = feature_description.get('applies_to', [])
        feature.units = feature_description.get('units', [])
        feature.logic = feature_description.get('logic', [])
        result.append(feature)
    return result


def _get_feature_names(features):
    return [feature.name for feature in features]


def _print_feature_names(feature_names):
    for name in feature_names:
        print(name)


def _load_resources(resources):
    for side in ['source', 'target']:
        resources[side].load_resources()
    return resources


def _get_resources(config):
    resources = {}
    for side in ('source', 'target'):
        resources[side] = Resources()
        resources[side].paths['language_model'] = config['resources'].get('{}_language_model'.format(side), None)
        resources[side].paths['lexical_table'] = config['resources'].get('{}_lexical_table'.format(side), None)
    return resources


def _read_feature_configuration(path):
    with open(path) as f:
        config = yaml.load(f)
    return _get_features(config), _get_resources(config)


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--src_path', help='source path'
    )
    parser.add_argument(
        '-t', '--tgt_path', help='target path'
    )
    parser.add_argument(
        '-o', '--out_path', help='output path'
    )
    parser.add_argument(
        '-c', '--config_path', help='configuration path'
    )
    return parser.parse_args()


def main():
    paths = _parse_arguments()
    features, resources = _read_feature_configuration(paths.config_path)
    resources_loaded = _load_resources(resources)
    out = open(paths.out_path, 'w')
    feature_names = []
    for source, target in zip(open(paths.src_path), open(paths.tgt_path)):
        results = {}
        for feature in features:
            if feature.feature_type == 'simple':
                executor = SimpleFeatureExecutor(source, target, feature, resources_loaded)
            else:
                executor = ComplexFeatureExecutor(source, target, feature, resources_loaded)
            results.update(executor.run())
        if not feature_names:
            feature_names = sorted(results.keys())
            out.write('\t'.join(feature_names))
        out.write('\t'.join(['{}'.format(results[k]) for k in feature_names]) + '\n')
    _print_feature_names(feature_names)
    out.close()


if __name__ == '__main__':
    main()
