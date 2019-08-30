import argparse
import sys

from parallel_data_cleaning.classifier import Classifier
from parallel_data_cleaning.utils import parse_args_with_help


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--features', required=True, type=str)
    parser.add_argument('-m', '--model', required=True, type=str)
    parser.add_argument('-o', '--output', required=False, type=str)
    args = parse_args_with_help(parser)

    stream = open(args.output, 'w') if args.output else sys.stdout

    classifier = Classifier()
    classifier.load_model(args.model)
    for row in classifier.lazy_load(args.features):
        pred = classifier._classifier.predict_proba([row])
        stream.write(pred[0][1])


if __name__ == '__main__':
    main()
