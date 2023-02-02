import config
import data_uploading
import gpudb


def check_for_primary_key(table_obj, gdf):

    try:
        res = table_obj.get_records_by_column(
            ["title"],
            offset=0,
            limit=-9999,
            encoding='binary',
            options={},
            print_data=False,
            force_primitive_return_types=True,
            get_column_major=True
        )
        res = res["title"]
    except gpudb.GPUdbException as e:
        print("failure: {}".format(str(e)))

    for i, row in gdf.iterrows():
        prk = row['title']
        found = 0
        for v in res:
            if prk == v:
                found = 1
        try:
            found = 1 / found
        except:
            print("failure in finding a record!")
    # print(res)

    return 1


