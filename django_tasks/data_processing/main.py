import data_acquisition
from data_validation import AqiDataValidation
from data_preprocessing import AqiDataPreprocess
import geopandas

from django_tasks.data_processing.data_uploading import UploadAqiData

if __name__ == '__main__':
    lij = data_acquisition.get_aqi_data()
    valid = AqiDataValidation(lij).execute()
    if valid:
        gdf = AqiDataPreprocess(lij).execute()
        table_obj = UploadAqiData.upload_data(gdf)




