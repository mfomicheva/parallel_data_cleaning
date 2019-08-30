import argparse

from parallel_data_cleaning.classifier import Classifier
from parallel_data_cleaning.utils import parse_args_with_help


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--positive_features_path', help='positive features path')
    parser.add_argument('-n', '--negative_features_path', help='negative features path')
    parser.add_argument('-o', '--out_path', help='output prefix')
    paths = parse_args_with_help(parser)
    classifier = Classifier()
    positive_features = classifier.load_features(paths.positive_features_path)
    negative_features = classifier.load_features(paths.negative_features_path)
    classifier.train_model(positive_features, negative_features)
    classifier.save_model(paths.out_path)


if __name__ == '__main__':
    main()
