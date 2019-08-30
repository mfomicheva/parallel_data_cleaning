import csv
import pickle
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics.classification import f1_score


class Classifier:

    def __init__(self):
        self._classifier = GradientBoostingClassifier()

    def train_model(self, positive_X, negative_X):
        features = np.concatenate((positive_X, negative_X), axis=0)
        labels = np.concatenate((
            np.ones((len(positive_X), 1)),
            np.zeros((len(negative_X), 1)),
        ))
        x_train, x_test, y_train, y_test = train_test_split(
            features, labels, train_size=0.7)
        self._classifier.fit(x_train, y_train)
        preds = self._classifier.predict(x_test)
        print('F1: {}'.format(f1_score(y_test, preds)))

    def save_model(self, path):
        pickle.dump(self._classifier, open(path, 'wb'))

    def load_model(self, path):
        self._classifier = pickle.load(open(path, 'rb'))

    @staticmethod
    def load_features(path):
        output = []
        with open(path) as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader, None)
            for row in reader:
                output.append([float(r) for r in row])
        f.close()
        return np.asarray(output)

    @staticmethod
    def lazy_load(path):
        with open(path) as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader, None)
            for row in reader:
                yield np.asarray([float(r) for r in row])
