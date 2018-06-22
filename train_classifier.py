import argparse

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


def main():
    paths = _parse_arguments()
    classifier = Classifier()
    positive_features = classifier.load_features(paths.positive_features_path)
    negative_features = classifier.load_features(paths.negative_features_path)
    classifier.train_model(positive_features, negative_features)
    classifier.save_model(paths.out_path)


if __name__ == '__main__':
    main()
