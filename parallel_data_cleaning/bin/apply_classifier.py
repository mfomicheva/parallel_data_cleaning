import argparse
import sys

from sklearn.metrics.classification import f1_score

from parallel_data_cleaning.classifier import Classifier
from parallel_data_cleaning.classifier import lazy_load_features
from parallel_data_cleaning.utils import parse_args_with_help


def predict(features, classifier=None, threshold=None):
    if classifier:
        pred = classifier._classifier.predict([features])[0]
        proba = classifier._classifier.predict_proba([features])[0][1]
        return pred, proba
    else:
        assert len(features) == 1
        pred = 1 if features[0] >= threshold else 0
        return pred, features[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--features', required=True, type=str)
    parser.add_argument('-o', '--output', required=False, type=str)
    parser.add_argument('-p', '--probas', required=False, action='store_true')
    parser.add_argument('-l', '--labels', required=False, default=None)
    parser.add_argument('-t', '--threshold', required=False, default=None, type=float)
    parser.add_argument('-m', '--model', required=False, default=None, type=str)
    args = parse_args_with_help(parser)

    stream = open(args.output, 'w') if args.output else sys.stdout

    classifier = None
    threshold = None
    if args.threshold:
        threshold = args.threshold
    else:
        classifier = Classifier()
        classifier.load_model(args.model)
    preds = []
    for row in lazy_load_features(args.features):
        pred, proba = predict(row, classifier=classifier, threshold=threshold)
        preds.append(pred)
        out = [pred, proba] if args.probas else [pred]
        stream.write('{}\n'.format('\t'.join(['{}'.format(o) for o in out])))
    if args.labels:
        labels = [int(l.strip()) for l in open(args.labels)]
        print('F1: {:.4f}'.format(f1_score(labels, preds)))


if __name__ == '__main__':
    main()
