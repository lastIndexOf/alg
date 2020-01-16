from sklearn.svm import LinearSVC, LinearSVR, SVC, SVR
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_moons

import matplotlib.pyplot as plt

x, y = make_moons(100, noise=.5)
