import data_acquisition
from data_validation import AqiDataValidation
from data_preprocessing import AqiDataPreprocess
import geopandas

if __name__ == '__main__':
    lij = data_acquisition.get_aqi_data()
    valid = AqiDataValidation(lij).execute()
    if valid:
        gdf = AqiDataPreprocess(lij).execute()
        print(gdf)



