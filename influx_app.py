import os

from influxdb import InfluxDBClient 

from .config import DefaultConfig


configuration = DefaultConfig

influx_client = InfluxDBClient(
    configuration.INFLUX_HOST,
    configuration.INFLUX_PORT,
    configuration.INFLUX_USER,
    configuration.INFLUX_PASSWORD,
    configuration.INFLUX_DB,
    ssl=configuration.INFLUX_USE_SSL,
)