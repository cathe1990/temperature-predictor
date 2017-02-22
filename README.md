#  Predictor: Weather Forecast of My Room

Temperature-predictor is a weather forecast tool applying machine learning algorithms with data collected from [Netatmo](https://www.netatmo.com/en-US/product/weather/weatherstation).

A few samples of my-own room weather forecast, Temperature-predictor:

```python
>>> from predictor.api import Model
>>> import datetime as dt
>>> predict_time = dt.datetime.now() + dt.timedelta(hours=1)
>>> model = Model()
>>> predict_result = model.predict(predict_time)
18
```

## Features

Temperature-predictor is a toolset for monitoring and forecast the inside temperature. (Netatmo Needed!)

- Get latest room temperature
- Get room temperature records within specific period
- Predict room temperature at specific future time

## Useage

Simply download the folder.

**The setup.py support is on the way.**

## What is Next
