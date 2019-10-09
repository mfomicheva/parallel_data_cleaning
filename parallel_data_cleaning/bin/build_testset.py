import argparse
from parallel_data_cleaning.utils import parse_args_with_help


def write_feats(path, out_fh):
    count = 0
    for line in open(path):
        out_fh.write('{}\n'.format(line.strip()))
        count += 1
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--positive_features_path', help='positive features path')
    parser.add_argument('-n', '--negative_features_path', help='negative features path')
    parser.add_argument('-o', '--out_pref', help='output prefix')
    args = parse_args_with_help(parser)
    out_feat_fh = open(args.out_pref + '.feats', 'w')
    pos_feat_cnt = write_feats(args.positive_features_path, out_feat_fh)
    neg_feat_cnt = write_feats(args.negative_features_path, out_feat_fh)
    out_feat_fh.close()
    out_labels_fh = open(args.out_pref + '.labels', 'w')
    for i in range(pos_feat_cnt):
        out_labels_fh.write('1\n')
    for i in range(neg_feat_cnt):
        out_labels_fh.write('0\n')
    out_labels_fh.close()


if __name__ == '__main__':
    main()
