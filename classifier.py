import pickle
import numpy as np

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics.classification import precision_score
from sklearn.metrics.classification import recall_score
from sklearn.metrics.classification import f1_score


class Classifier:

    def __init__(self):
        self._classifier = GradientBoostingClassifier()

    def train_model(self, positive_X, negative_X):
        for i in range(1, 49):
            features = np.concatenate((positive_X[:, :i], negative_X[:, :i]), axis=0)
            labels = np.concatenate((
                np.ones((len(positive_X), 1)),
                np.zeros((len(negative_X), 1)),
            ))
            x_train, x_test, y_train, y_test = train_test_split(
                features, labels, train_size=0.7)
            self._classifier.fit(x_train, y_train)
            preds = self._classifier.predict(x_test)
            print('{}: {}'.format(i, f1_score(y_test, preds)))

    def save_model(self, path):
        pickle.dump(self._classifier, open(path, 'wb'))
