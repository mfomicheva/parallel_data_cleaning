import argparse
import sys
import re
import importlib

from features.feature_names import feature_names


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--src_path', help='source path'
    )
    parser.add_argument(
        '-t', '--tgt_path', help='target path'
    )
    parser.add_argument(
        '-slm', '--source_lang_model', help='source language model',
        default='toy_resources/lm.tok.en'
    )
    parser.add_argument(
        '-tlm', '--target_lang_model', help='target language model',
        default='toy_resources/lm.tok.de'
    )
    return parser.parse_args()


def _load_feature_class(feature_name):
    try:
        module = importlib.import_module('features.' + feature_name)
        my_class = getattr(module, _snake_to_camel(feature_name))
        return my_class
    except KeyError:
        sys.stderr('No feature with the name %s is defined', feature_name)
        return None


def _snake_to_camel(name):
    return re.sub(r'(?:^|_)(\w)', lambda x: x.group(1).upper(), name)


def main():
    args = _parse_arguments()
    with open(args.src_path) as f_src:
        with open(args.tgt_path) as f_tgt:
            for src, tgt in zip(f_src.readlines(), f_tgt.readlines()):
                results = []
                for feature_name in feature_names:
                    feature = _load_feature_class(feature_name)(src, tgt)
                    feature.run()
                    results.append(feature)
                sys.stdout.write('{}\n'.format('\t'.join(['{}'.format(r.score) for r in results])))


if __name__ == '__main__':
    main()
