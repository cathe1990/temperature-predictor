# _*_ coding: utf-8 _*_

from __future__ import print_function

import pytest
from simulator import rawdata


def test_raw_data(raw_data_folder='./rawdata'):
    """Test rawdata.RawData class"""
    raw_data = rawdata.RawData(raw_data_folder=raw_data_folder)
    assert len(raw_data) == 9
    assert set(raw_data.sources) == set(['air_conditioner', 'wunderground', 'weather_station'])
    assert set(raw_data.monitors) == set(['kitamura', 'wada', 'tsuda'])
    assert set(raw_data.datatypes) == set(['inside', 'outside', 'onaircon', 'log', 'weather'])

