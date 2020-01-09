# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score

from math import sqrt
from collections import Counter
from sklearn import datasets
import numpy as np


class KNeighborsClassifier:
    def __init__(self, k):
        self.k = k
        self.__X_train = None
        self.__y_train = None

    def fit(self, X_train, y_train):
        self.__X_train = X_train
        self.__y_train = y_train

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return accuracy_score(y_test, y_predict)

    def predict(self, X_predict):
        y_predict = [self.__predict_one(x) for x in X_predict]
        return y_predict

    def __predict_one(self, x_predict):
        distances = [sqrt(np.sum((X-x_predict)**2)) for X in self.__X_train]
        sorted_indexes = np.argsort(distances)

        min_distance = self.__y_train[sorted_indexes][:self.k]
        counter = Counter(min_distance)

        return counter.most_common(1)[0][0]


def train_test_split(X_sample, y_sample, test_size=0.2):
    assert len(X_sample) == len(y_sample), '/'

    test_len = int(len(X_sample) * test_size)
    shuffle_indexes = np.random.permutation(len(X_sample))

    X_train = X_sample[shuffle_indexes[test_len:]]
    y_train = y_sample[shuffle_indexes[test_len:]]

    X_test = X_sample[shuffle_indexes[:test_len]]
    y_test = y_sample[shuffle_indexes[:test_len]]

    return X_train, X_test, y_train, y_test


def accuracy_score(y_test, y_predict):
    assert len(y_test) == len(y_predict), '/'

    correct_len = np.sum(y_test == y_predict)

    return correct_len / len(y_test)


digits = datasets.load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

knn_clf = KNeighborsClassifier(6)
knn_clf.fit(X_train, y_train)

print(knn_clf.score(X_test, y_test))
