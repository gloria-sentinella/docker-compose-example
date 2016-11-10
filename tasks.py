from __future__ import absolute_import
import StringIO
import base64
from datetime import datetime
from medusa.celery import app
from medusa.influx_app import influx_client

@app.task
def add_metrics():
    json_body = []
        metric_timestamp = datetime.fromtimestamp(float(1335552733.000)).strftime(time_string_format)
        json_body.append({'measurement': 'test',
         'tags': {'server_id': '100',
                  'account_key': "jsjjsjsjsjsjsjs"},
         'fields': {'value':"Hola",
                    'local_timestamp': metric_timestamp}})

    resp = influx_client.write_points(json_body)
    return resp