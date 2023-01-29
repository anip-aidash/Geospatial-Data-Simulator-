import config
from abc import ABC, abstractmethod
import geopandas
import pandas


class DataPreprocess(ABC):
    def __init__(self, list_of_json):
        self.list_of_json = list_of_json

    @abstractmethod
    def create_dataframe(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class AqiDataPreprocess(DataPreprocess):
    def __init__(self, list_of_json):
        super().__init__(list_of_json)
        self.dataframe = None
        self.geo_dataframe = None

    def create_dataframe(self):
        self.dataframe = pandas.DataFrame(columns=config.aqi_columns)
        for json_data in self.list_of_json:
            new_row = {'city': json_data['city_name'], 'lat': json_data['lat'], 'lon': json_data['lon'],
                       'aqi': json_data['data'][0]['aqi'], 'timestamp': json_data['timestamp']}
            self.dataframe.loc[len(self.dataframe)] = new_row

    def update_aqi_status(self):
        for i, row in self.dataframe.iterrows():
            aqi = row['aqi']
            status = ''
            if aqi <= 17:
                status = "Good"
            elif aqi <= 35:
                status = "Moderate"
            else:
                status = "Poor"
            self.dataframe.at[i, 'status'] = status

    def add_title_as_primary_key(self):
        for i, row in self.dataframe.iterrows():
            title = str(row['timestamp'])
            title = title + '#'
            title = title + config.std_code[row['city']]
            self.dataframe.at[i, 'title'] = title

    def add_geometry(self):
        self.geo_dataframe = geopandas.GeoDataFrame(self.dataframe,
                                                    geometry=geopandas.points_from_xy(self.dataframe.lon,
                                                                                      self.dataframe.lat))

    def execute(self):
        self.create_dataframe()
        self.update_aqi_status()
        self.add_title_as_primary_key()
        self.add_geometry()

        return self.geo_dataframe


if __name__ == '__main__':
    lij = [{'city_name': 'Ranchi', 'country_code': 'IN', 'data': [
        {'aqi': 16, 'co': 233.6502, 'mold_level': 0, 'no2': 0.037485734, 'o3': 26.82209, 'pm10': 7.150768,
         'pm25': 3.739839, 'pollen_level_grass': 0, 'pollen_level_tree': 0, 'pollen_level_weed': 0,
         'predominant_pollen_type': 'Molds', 'so2': 0.46938658}], 'lat': '23.34316', 'lon': '85.3094',
            'state_code': '38', 'timezone': 'Asia/Kolkata'}, {'city_name': 'Delhi', 'country_code': 'IN', 'data': [
        {'aqi': 45, 'co': 180.24445, 'mold_level': 0, 'no2': 0.011379598, 'o3': 26.464462, 'pm10': 14.3423815,
         'pm25': 10.756786, 'pollen_level_grass': 0, 'pollen_level_tree': 0, 'pollen_level_weed': 0,
         'predominant_pollen_type': 'Molds', 'so2': 0.51409006}], 'lat': '28.65195', 'lon': '77.23149',
                                                              'state_code': '07', 'timezone': 'Asia/Kolkata'},
           {'city_name': 'Jaipur', 'country_code': 'IN', 'data': [
               {'aqi': 22, 'co': 181.91338, 'mold_level': 0, 'no2': 0.01121225, 'o3': 23.60344, 'pm10': 10.859395,
                'pm25': 5.260744, 'pollen_level_grass': 0, 'pollen_level_tree': 0, 'pollen_level_weed': 0,
                'predominant_pollen_type': 'Molds', 'so2': 0.5289912}], 'lat': '26.91962', 'lon': '75.78781',
            'state_code': '24', 'timezone': 'Asia/Kolkata'}, {'city_name': 'Bangalore', 'country_code': 'IN', 'data': [
            {'aqi': 14, 'co': 210.28519, 'mold_level': 0, 'no2': 0.01740409, 'o3': 29.325485, 'pm10': 3.543453,
             'pm25': 1.4764396, 'pollen_level_grass': 0, 'pollen_level_tree': 0, 'pollen_level_weed': 0,
             'predominant_pollen_type': 'Molds', 'so2': 0.22165477}], 'lat': '12.97194', 'lon': '77.59369',
                                                              'state_code': '19', 'timezone': 'Asia/Kolkata'},
           {'city_name': 'Surat', 'country_code': 'IN', 'data': [
               {'aqi': 7, 'co': 188.5891, 'mold_level': 0, 'no2': 0.008367351, 'o3': 15.556812, 'pm10': 0.9344986,
                'pm25': 0.5, 'pollen_level_grass': 0, 'pollen_level_tree': 0, 'pollen_level_weed': 0,
                'predominant_pollen_type': 'Molds', 'so2': 0.022584572}], 'lat': '21.19594', 'lon': '72.83023',
            'state_code': '09', 'timezone': 'Asia/Kolkata'}, {'city_name': 'Kolkata', 'country_code': 'IN', 'data': [
            {'aqi': 26, 'co': 201.94054, 'mold_level': 0, 'no2': 0.025771443, 'o3': 25.749207, 'pm10': 8.197899,
             'pm25': 6.148424, 'pollen_level_grass': 0, 'pollen_level_tree': 0, 'pollen_level_weed': 0,
             'predominant_pollen_type': 'Molds', 'so2': 0.17508864}], 'lat': '22.56263', 'lon': '88.36304',
                                                              'state_code': '28', 'timezone': 'Asia/Kolkata'}]

    obj = AqiDataPreprocess(lij)
    obj.execute()
