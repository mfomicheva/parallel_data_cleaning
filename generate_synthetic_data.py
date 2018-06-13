import argparse

from random import randint


operations = ('swap', 'copy_source', 'copy_target','random_source', 'random_target')


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


def read_file(path):
    return [l.strip() for l in open(path).readlines()]


def generate_synthetic_data(src_path, tgt_path, outpath_src, outpath_tgt):
    sources = read_file(src_path)
    targets = read_file(tgt_path)
    assert len(sources) == len(targets)
    out_src = open(outpath_src, 'w')
    out_tgt = open(outpath_tgt, 'w')
    for src, tgt in zip(sources, targets):
        operation = operations[randint(0, 4)]
        negative_pair = None
        if operation == 'swap':
            negative_pair = (tgt, src)
        elif operation == 'copy_source':
            negative_pair = (src, src)
        elif operation == 'copy_target':
            negative_pair = (tgt, tgt)
        elif operation == 'random_source':
            negative_pair = (sources[randint(0, len(sources) - 1)], tgt)
        elif operation == 'random_target':
            negative_pair = (src, targets[randint(0, len(targets) - 1)])
        else:
            pass
        out_src.write('{}\n'.format(negative_pair[0]))
        out_tgt.write('{}\n'.format(negative_pair[1]))
    out_src.close()
    out_tgt.close()


def main():
    args = parse_arguments()
    generate_synthetic_data(
        args.src_path, args.tgt_path, args.out_path_src, args.out_path_tgt)


if __name__ == '__main__':
    main()
