import json
import datetime


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import gpudb

from . import config


@api_view(['GET'])
def get_latest(request):
    options = gpudb.GPUdb.Options()
    options.username = config.database_username
    options.password = config.database_password

    DATABASE = gpudb.GPUdb(
        host=["http://localhost:9191"],
        options=options
    )

    results = []
    for city in config.cities:
        try:
            query_expr = "select * from " + config.aqi_schema_name + "." + config.aqi_table_name + " where city = '" + city + "' order by timestamp limit 1"
            # print(query_expr)
            res = DATABASE.execute_sql_and_decode(
                statement=query_expr,
                offset=0,
                limit=1,
                encoding='binary',
                request_schema_str='',
                data=[],
                options={}
            ).records
            results.append(res)
        except gpudb.GPUdbException as e:
            print("failure: {}".format(str(e)))

    for result in results:
        for key, value in result.items():
            result[key] = value[0]

    json_object = json.dumps(results)
    return Response(json_object)

@api_view(['GET'])
def get_latest_data_by_timestamp(request, timestamp):
    # data = request.GET.get('timestamp')
    data = datetime.datetime.fromtimestamp(int(timestamp)).date()
    new_date = "'"
    new_date += str(data)
    new_date += "'"

    options = gpudb.GPUdb.Options()
    options.username = config.database_username
    options.password = config.database_password

    DATABASE = gpudb.GPUdb(
        host=["http://localhost:9191"],
        options=options
    )

    results = []
    for city in config.cities:
        try:
            query_expr = "select * from " + config.aqi_schema_name + "." + config.aqi_table_name + " where city = '" + city + "' order by " + "ABS(TIMESTAMPDIFF(SECOND, " + new_date + ", timestamp)) asc " + " limit 1"
            # print(query_expr)
            res = DATABASE.execute_sql_and_decode(
                statement=query_expr,
                offset=0,
                limit=1,
                encoding='binary',
                request_schema_str='',
                data=[],
                options={}
            ).records
            print(res)
            results.append(res)
        except gpudb.GPUdbException as e:
            print("failure: {}".format(str(e)))
    # print(results)
    for result in results:
        for key, value in result.items():
            result[key] = value[0]

    json_object = json.dumps(results)
    return Response(json_object)
