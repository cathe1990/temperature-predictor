# _*_ coding: utf-8 _*_

import lnetatmo
from .params import infos


def last_record():
    """Get latest record of netatmo"""
    authorization = lnetatmo.ClientAuth(clientId=infos.client_id,
                                        clientSecret=infos.client_secret,
                                        username=infos.username,
                                        password=infos.password,
                                        scope="")
    weather_station = lnetatmo.WeatherStationData(authorization)

    # Get dashboard data by device_id
    weather_station_dashboard_data = weather_station.stationById(sid=infos.device_id)

    return weather_station_dashboard_data['dashboard_data']


def get_record(start_time,
               end_time,
               scale='30min',
               record_type='Temperature,Humidity'):
    """Get records of given period of time
    :params start_time: the start point of records
    :type start_time: datetime.datetime

    :params end_time: the end point of records
    :type end_time: datetime.datetime

    :params scale: the interval between two records
    :type scale: string, e.g. 10min, 5min, etc.

    :params record_type: the type of weather information
    :type record_type: string

    :return: list of tuple (timestamp, temperature, humidity)
    """
    authorization = lnetatmo.ClientAuth(clientId=infos.client_id,
                                        clientSecret=infos.client_secret,
                                        username=infos.username,
                                        password=infos.password,
                                        scope="")
    weather_station = lnetatmo.WeatherStationData(authorization)

    resp = weather_station.getMeasure(device_id=infos.device_id,
                                      scale=scale,
                                      mtype=record_type,
                                      date_begin=start_time,
                                      date_end=end_time)
    # return the result in the format of tuple, (timestamp, temperature, humidity)
    result = [(int(k), v[0], v[1]) for k, v in resp['body'].items()]
    # sort the records by timestamp
    result.sort()
    return result

