import requests
import config
import calendar
import time


def get_aqi_data():
    list_of_json = []
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    for city in config.cities:
        try:
            url = "https://api.weatherbit.io/v2.0/current/airquality?key=%s&city=%s" % (config.aqi_api_key, city)
            response = requests.get(url)
            json_data = response.json()
            json_data['timestamp'] = time_stamp
            list_of_json.append(json_data)
        except requests.exceptions.HTTPError as errh:
            print(errh)
            break
        except requests.exceptions.ConnectionError as errc:
            print(errc)
            break

    return list_of_json
