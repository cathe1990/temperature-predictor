# _*_ coding:utf-8 _*_

"""
Basic Machine learning alogrithms
"""

from sklearn import (tree, linear_model)


def linear_regression(x, y):
    linear = linear_model.LinearRegression()
    linear.fit(x, y)

    return linear


def decision_tree_regression(x, y):
    clf = tree.DecisionTreeRegressor()
    clf.fit(x, y)

    return clf

