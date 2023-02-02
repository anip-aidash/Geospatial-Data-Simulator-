import gpudb
import config
import datetime

options = gpudb.GPUdb.Options()
options.username = config.database_username
options.password = config.database_password

DATABASE = gpudb.GPUdb(
    host=["http://localhost:9191"],
    options=options
)


class UploadAqiData:
    @staticmethod
    def upload_data(gdf):

        # extract columns
        col = gdf.columns.tolist()

        col_schema = []
        for c in col:
            if c == "title":
                col_schema.append([c, "string", "char64", "primary_key"])
            elif c == "timestamp":
                col_schema.append([c, "string", "datetime"])
            else:
                col_schema.append([c, "string", "char64"])

        no_error_option = {"no_error_if_not_exists": "true"}

        DATABASE.clear_table(table_name=config.aqi_table_name, options=no_error_option)

        try:
            table_obj = gpudb.GPUdbTable(
                _type=col_schema,
                name=config.aqi_table_name,

                options={
                    "collection_name": config.aqi_schema_name,
                    "is_replicated": "false"
                },

                db=DATABASE
            )
        except gpudb.GPUdbException as e:
            print("table creation failure: {}".format(str(e)))

        # insertion into aqi_table
        records = []
        for i, row in gdf.iterrows():
            record = []
            cnt = 0
            for r in row:
                cnt += 1
                if cnt == 2:
                    r = int(r)
                    time_stamp = datetime.datetime.utcfromtimestamp(r).strftime('%Y-%m-%d %H:%M:%S')
                    record.append(time_stamp)
                else:
                    record.append(r)
            records.append(record)

        for record in records:
            table_obj.insert_records(record)

        return table_obj
