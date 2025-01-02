# locations of everything

import modelmgr

# DATA_BASEPATH = "/mnt/c/Users/nearw/data/population/"
DATA_BASEPATH = "/Users/dd/pCloud Drive/data/population/"
# DATA_BASEPATH = "/home/dd/pCloudDrive/data/population/"

COUNTRY_PATH = 'data/country/'
GLOBAL_PATH = 'data/global/'
METADATA_PATH = 'data/metadata/'

GLOBAL_TEMPLATE = "{}_global_{}.csv"
COUNTRY_TEMPLATE = "{}_country_{}.csv"

# specific filenames

LOADED_MODELS_FILENAME = "loaded_models.json"
LOCATIONS_FILENAME = "location.json"
GLOBAL_ALL_FILENAME = "all_global.csv"


def get_file_path(dataset, name):
    ds = modelmgr.model_files(name)
    datasetpath = ds['basepath'] + ds['path']
    filepath = ds['data']['files'][name]
    return(datasetpath + filepath)

def get_coll_file_path(dataset, coll, val):
    ds = modelmgr.model_files(name)
    datasetpath =  DATA_BASEPATH + ds['path']
    base_filepath = ds['data']['collections'][coll]['basepath']
    filepath = base_filepath.format(val)
    return(datasetpath + filepath)
    
# return the full path if someone already has the filepath and scenario
def get_scenario_file_path(filepath, scenario):
    return DATA_BASEPATH + filepath.format(scenario)
    
# return the global path for a model+scenario combo
def get_global_path(model, scenario):
    filename = GLOBAL_TEMPLATE.format(model, scenario)
    return(DATA_BASEPATH + GLOBAL_PATH + filename)
    
# return the global path that holds all data
def get_global_all_path():
    return(DATA_BASEPATH + GLOBAL_PATH + GLOBAL_ALL_FILENAME)


# return the country path for a model+scenario combo
def get_country_path(model, scenario):
    filename = COUNTRY_TEMPLATE.format(model, scenario)
    return(DATA_BASEPATH + COUNTRY_PATH + filename)
    
# return the metadata path
def get_loaded_models_path():
    return(DATA_BASEPATH + METADATA_PATH + LOADED_MODELS_FILENAME)

# get locations path
def get_locations_path():
    return(DATA_BASEPATH + METADATA_PATH + LOCATIONS_FILENAME)

def get_coll_vals(dataset, coll):
    ds = modelmgr.model_files(name)
    return(ds['data']['collections'][coll]['vals'])
