cities = ['Ranchi', 'Delhi', 'Jaipur', 'Bangalore', 'Surat', 'Kolkata']
std_code = {'Ranchi': '0651', 'Delhi': '011', 'Jaipur': '141', 'Bangalore': '080', 'Surat': '0261', 'Kolkata': '33'}
aqi_api_key = "2c92c90678b746a6af369ab3ca10ed5c"

aqi_columns = ['title', 'timestamp', 'city', 'aqi', 'status', 'lat', 'lon']
aqi_json_keys = ['lat', 'lon', 'city', 'data']

aqi_json_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "timestamp": {
            "type": "integer"
        },
        "city_name": {
            "type": "string"
        },
        "country_code": {
            "type": "string"
        },
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "aqi": {
                            "type": "integer"
                        },
                        "co": {
                            "type": "number"
                        },
                        "mold_level": {
                            "type": "integer"
                        },
                        "no2": {
                            "type": "number"
                        },
                        "o3": {
                            "type": "number"
                        },
                        "pm10": {
                            "type": "number"
                        },
                        "pm25": {
                            "type": "number"
                        },
                        "pollen_level_grass": {
                            "type": "integer"
                        },
                        "pollen_level_tree": {
                            "type": "integer"
                        },
                        "pollen_level_weed": {
                            "type": "integer"
                        },
                        "predominant_pollen_type": {
                            "type": "string"
                        },
                        "so2": {
                            "type": "number"
                        }
                    },
                    "required": [
                        "aqi"
                    ]
                }
            ]
        },
        "lat": {
            "type": "string"
        },
        "lon": {
            "type": "string"
        },
        "state_code": {
            "type": "string"
        },
        "timezone": {
            "type": "string"
        }
    },
    "required": [
        "timestamp",
        "city_name",
        "country_code",
        "data",
        "lat",
        "lon",
        "state_code",
        "timezone"
    ]
}
