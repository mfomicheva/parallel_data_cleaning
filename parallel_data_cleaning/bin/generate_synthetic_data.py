import argparse

from parallel_data_cleaning.generate_synthetic_data import generate_synthetic_data
from parallel_data_cleaning.utils import parse_args_with_help



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--src_path', help='source path',
        default='toy_corpus/src.en'
    )
    parser.add_argument(
        '-t', '--tgt_path', help='target path',
        default='toy_corpus/tgt.de'
    )
    parser.add_argument(
        '-os', '--out_path_src', help='output path source',
        default='output/src.neg.en'
    )
    parser.add_argument(
        '-ot', '--out_path_tgt', help='output path target',
        default='output/tgt.neg.en'
    )
    return parser.parse_args()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--src_path', help='source path', default='toy_corpus/src.en')
    parser.add_argument('-t', '--tgt_path', help='target path', default='toy_corpus/tgt.de')
    parser.add_argument('-os', '--out_path_src', help='output path source', default='output/src.neg.en')
    parser.add_argument('-ot', '--out_path_tgt', help='output path target', default='output/tgt.neg.en')
    args = parse_args_with_help(parser)
    generate_synthetic_data(args.src_path, args.tgt_path, args.out_path_src, args.out_path_tgt)


if __name__ == '__main__':
    main()
