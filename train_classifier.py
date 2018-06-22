import argparse
import csv
import numpy as np

from classifier import Classifier


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--positive_features_path', help='positive features path'
    )
    parser.add_argument(
        '-n', '--negative_features_path', help='negative features path'
    )
    parser.add_argument(
        '-o', '--out_path', help='output prefix'
    )
    return parser.parse_args()


def _load_features(path):
    output = []
    with open(path) as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader, None)
        for row in reader:
            output.append([float(r) for r in row])
    f.close()
    return np.asarray(output)


def main():
    paths = _parse_arguments()
    positive_features = _load_features(paths.positive_features_path)
    negative_features = _load_features(paths.negative_features_path)
    classifier = Classifier()
    classifier.train_model(positive_features, negative_features)
    classifier.save_model(paths.out_path)


if __name__ == '__main__':
    main()
