from datetime import datetime as dt
import os
import json
import numpy as np

# https://github.com/hmallen/numpyencoder
class NumpyEncoder(json.JSONEncoder):
    """ Custom encoder for numpy data types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):

            return int(obj)

        elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
            return float(obj)
        
        elif isinstance(obj, (np.complex_, np.complex64, np.complex128)):
            return {'real': obj.real, 'imag': obj.imag}
        
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
    
        elif isinstance(obj, (np.bool_)):
            return bool(obj)

        elif isinstance(obj, (np.void)): 
            return None

        return json.JSONEncoder.default(self, obj)

    
def create_django_datetimestamp(dt_object=None):
    
    if dt_object==None:
        created_time = dt.now()
    else:
        created_time = dt_object
    # for django, timefield must be in format YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
    # e.g. "2020-05-26T11:40:56+01:00"
    created_time = created_time.strftime('%Y-%m-%dT%H:%M:%S+01:00')
    
    return created_time


def df_to_json_list(df,
                    app_name,
                    model_name,
                    file_name_modifier='',
                    use_df_index_as_pk=False,
                    pk_start_num=1000,
                    create_datetimefield_name=None,
                    created_by_field_name=None,
                    created_by_value=1):
    
    """
    convert a dataframe to a django fixture file to populate an database
    each column becomes a field in the record
    
    df,
    app_name: app name in django,
    model_name: model name in django
    folder: destination folder to output files to
    use_df_index_as_pk: if True df.index will become the primary key for records
    no checks are performed
    pk_start_num: if use_df_index_as_pk is False, primary keys will start at this
    number
    create_datetimefield_name: set to the name of the datetimefield for
    recording when a record is created.
    """

    model = "{}.{}".format(app_name, model_name)
    
    if create_datetimefield_name:
        created_time = create_django_datetimestamp()
        df[create_datetimefield_name] = created_time
    
    if created_by_field_name:
        df[created_by_field_name] = created_by_value
    
    fixture_lst = []
    for i, row in df.reset_index().iterrows():
        
        if use_df_index_as_pk==True:       
            pk = row['index']
        
        else:
            pk = i+pk_start_num
        
        fields_ser = row.drop(['index']).dropna()
        fields_dict =  fields_ser.to_dict()
        
        record = {'model':model, 
               'pk':pk,
               'fields': fields_dict}
        fixture_lst.append(record)
        fname = model_name+'{}.json'.format(file_name_modifier)

    return fname, fixture_lst


def write_fixture_to_json( fixture_lst, fname, output_folder='default'):
    """

    fixture_lst: a list of records in the django fixture format
    output_folder: relative path to the output folder
    fname: name to save list to (including .json extension)
    """
    
    if output_folder=='default':
        output_folder='../data/processed/fixtures'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    fpath = os.path.join(output_folder, fname)
    
    if os.path.exists(fpath):
        raise FileExistsError('did not save, file already exists at: {}'.format(fpath))

    with open(fpath, 'w') as f:
        json.dump(fixture_lst, 
                  f, 
                  skipkeys=False, 
                  sort_keys=False, 
                  cls=NumpyEncoder,
                  )
        
    print(f'wrote fixture to {fpath}')
    return