# _*_ coding: utf-8 _*_

import pytest
from simulator import rawdata
from simulator.utils import (read_all_csv, noise_cancel, resample)


RAW_DATA = rawdata.RawData(raw_data_folder='./rawdata')
TEST_QUERY = "INSERT INTO d_control VALUES ('tojo', '2017/02/08 20:55', '2017/02/08 21:20', 'heating', 'auto', 'auto', '1', '-1', '2', 'uL8ahgIL38PeI6JvclbQ/VJb9B6ydRMPqB12aiTIFZU=', 'Type_F', 'None', '22', '2017/02/08 20:55', 'enable')"  # nopep8


def test_read_all_csv():
    """Test read_all_csv method"""
    data_dict = read_all_csv(raw_data=RAW_DATA)
    assert set(data_dict.keys()) == set(RAW_DATA.monitors)
    # **CAUTION: NEED DELETE LATER**
    # Save to local csv for later check


def test_schedule_air_conditioner_operation():
    """Test schedule_air_conditioner_operation"""
    import subprocess
    schedule_air_conditioner_operation(sql_query=TEST_QUERY)

    subprocess.run()

