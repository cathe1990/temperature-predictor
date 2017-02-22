# _*_ coding: utf-8 _*_

from .structures import LookupDict

_infos = {
    'username': 'somefay@gmail.com',
    'password': 'WeiChen0214',
    'client_id': '58a93034ee261c781b8b468b',
    'client_secret': 'OnS1A43sFwYj73jupbYUborT7M8cY',
    'device_id': '70:ee:50:05:e9:d0'
}

infos = LookupDict(name='user_infos')

for attr, value in _infos.items():
    setattr(infos, attr, value)›

