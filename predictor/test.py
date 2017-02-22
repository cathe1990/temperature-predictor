from . import netatmo
from .algorithms import basic_algorithm
import datetime as dt


def test():
    data = netatmo.get_record(start_time=dt.datetime(2015, 12, 1, 0, 0, 0),
                              end_time=dt.datetime(2016, 3, 1, 0, 0, 0))

    length = len(data)
    data_x = [[d[0], d[2]] for d in data][:int(0.7*length)]
    data_y = [d[1] for d in data][:int(0.7*length)]

    model = basic_algorithm.linear_regression(data_x, data_y)

    test_x = [[d[0], d[2]] for d in data][int(0.7*length):]
    test_y = [d[1] for d in data][int(0.7*length):]

    predict_y = model.predict(test_x)

    print(mean_square_error(test_y, predict_y))


def mean_square_error(y1, y2):
    diff_y = [(y1[i] - y2[i])**2 for i in range(len(y1))]
    return sum(diff_y)//len(diff_y)

