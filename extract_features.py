import pkgutil
import sys
import re
import importlib

from language_resources import LanguageResources
from parse_args import args


def _implemented_features_names():
    return [name for _, name, _ in pkgutil.iter_modules(['features']) if
            not name.startswith('base')]


def _load_feature_class(feature_name, src, tgt, resources):
    try:
        module = importlib.import_module('features.' + feature_name)
        feature = getattr(module, _snake_to_camel(feature_name))
        return feature(src, tgt, resources)
    except KeyError:
        sys.stderr('No feature with the name %s is defined', feature_name)
        return None


def _snake_to_camel(name):
    return re.sub(r'(?:^|_)(\w)', lambda x: x.group(1).upper(), name)


def main():
    resources = LanguageResources(args)
    for src, tgt in zip(open(args.src_path), open(args.tgt_path)):
        results = []
        for feature_name in _implemented_features_names():
            feature = _load_feature_class(
                feature_name, src.strip(), tgt.strip(), resources)
            feature.run()
            results.append(feature)
        sys.stdout.write('{}\n'.format('\t'.join(['{}'.format(r.score) for r in results])))


if __name__ == '__main__':
    main()
