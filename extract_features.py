import getopt
import sys
import re
import importlib

from features.feature_names import feature_names
from parse_args import args


def _read_args(args):
    opts, args = getopt.getopt(args, 'hs:t:ls:lt:', ['input_file='])
    path_src = None
    path_tgt = None
    for opt, arg in opts:
        if opt in ('-s', '--source_file'):
            path_src = arg
        elif opt in ('-t', '--target_file'):
            path_tgt = arg
        else:
            sys.stdout.write('-s <source_file> -t <target_file>')
            sys.exit()
    return path_src, path_tgt


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
