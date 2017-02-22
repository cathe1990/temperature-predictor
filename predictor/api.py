# _*_ coding: utf-8 _*_

"""
All apis are listed here
"""

from predictor.algorithms import basic_algorithm
import datetime as dt


class Model():
	def __init__(self, t1=dt.datetime(2015, 12, 1, 0, 0, 0), t2=dt.datetime(2016, 3, 1, 0, 0, 0), algorithm='lr'):
		data = netatmo.get_record(t1, t2)
		data_x = [dt.datetime.fromtimestamp(d[0]) for d in data]
		data_y = [d[1] for d in data]

		if algorithm == 'lr':
			model = basic_algorithm.linear_regression(data_x, data_y)
		else:
			model = basic_algorithm.decision_tree_regression(data_x, data_y)
		self.model = model

	def predict(self, t):
		result = self.model.predict(t)
		return result

