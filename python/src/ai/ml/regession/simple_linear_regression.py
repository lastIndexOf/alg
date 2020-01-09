import matplotlib.pyplot as plt
import numpy as np


class SimpleLinearRegression:
    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        self.a_ = (x_train - x_mean).dot(y_train - y_mean) / \
            (x_train - x_mean).dot(x_train - x_mean)
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        return np.array([self.__predict(x) for x in x_predict])

    def __predict(self, x):
        assert self.a_ is not None and self.b_ is not None, '/'

        return self.a_ * x + self.b_

    def __repr__(self):
        print('self.repr')


m = 100
x_train = np.random.random(m)
y_train = x_train * 3 + 2 + np.random.normal(0, 1, size=m)


sre = SimpleRegression()
sre.fit(x_train, y_train)

y_predict = sre.predict(x_train)

plt.scatter(x_train, y_train)
plt.plot(x_train, y_predict, color='r')
plt.show()
