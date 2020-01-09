from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
# from sklearn.metrics import mean_squared_error
from sklearn import datasets
import numpy as np


class LinearRegression:
    def __init__(self):
        self.__theta = None
        self.coef_ = None
        self.interception_ = None

    def fit(self, X_train, y_train):
        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])

        self.__theta = np.linalg.inv(X_b.T.dot(
            X_b)).dot(X_b.T).dot(y_train)

        self.coef_ = self.__theta[1:]
        self.interception_ = self.__theta[0]

    def predict(self, X_predict):
        X_b = np.hstack([np.ones(((len(X_predict), 1))), X_predict])

        return X_b.dot(self.__theta)

    def score(self, X_test, y_test):
        return r2_score(y_test, self.predict(X_test))

    def __predict(self):
        pass


def r2_score(y_test, y_predict):
    return 1 - mean_squared_error(y_test, y_predict) / np.var(y_test)


def mean_squared_error(y_test, y_predict):
    # return np.sum((y_test-y_predict)**2)/len(y_test)
    return (y_test-y_predict).dot(y_test-y_predict) / len(y_test)


boston = datasets.load_boston()

y = boston.target
X = boston.data[y < np.max(y)]
y = y[y < np.max(y)]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

linearRegression = LinearRegression()
linearRegression.fit(X_train, y_train)

knn_clf = KNeighborsRegressor()
knn_clf.fit(X_train, y_train)

print(linearRegression.score(X_test, y_test))
print(knn_clf.score(X_test, y_test))
