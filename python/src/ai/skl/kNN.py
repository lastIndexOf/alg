from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import datasets
from random import randint

import matplotlib.pyplot as plt


digits = datasets.load_digits()

X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2, random_state=66)

knn_cfr = KNeighborsClassifier(n_neighbors=6)
knn_cfr.fit(X_train, y_train)

print('socre = ', knn_cfr.score(X_test, y_test))
print('accuracy_score = ', accuracy_score(y_test, knn_cfr.predict(X_test)))

random_index = randint(0, 99)
x_sample = X_test[random_index]
y_sample = y_test[random_index]

print(x_sample.reshape(8, 8))
print(y_sample)

plt.imshow(x_sample.reshape(8, 8), cmap=plt.cm.bone)
plt.show()
