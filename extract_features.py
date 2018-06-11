import yaml
import argparse

from feature_executor import FeatureExecutor
from language_resources import load_language_resources


def _read_feature_configuration(path):
    with open(path) as f:
        config = yaml.load(f)
    return config


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
    return parser.parse_args()


def main():
    paths = _parse_arguments()
    config = _read_feature_configuration('feature_config.yml')
    language_resources = load_language_resources(config['resources'])
    feature_names = []
    out = open(paths.out_path, 'w')
    for source, target in zip(open(paths.src_path), open(paths.tgt_path)):
        executor = FeatureExecutor(source, target, config, language_resources)
        results = executor.execute()
        if not feature_names:
            feature_names = sorted(results.keys())
            print('\n'.join([f for f in feature_names]))
        out.write('\t'.join(['{}'.format(results[k]) for k in feature_names]) + '\n')
    out.close()


if __name__ == '__main__':
    main()
