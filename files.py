# locations of everything

import modelmgr

# DATA_BASEPATH = "/mnt/c/Users/nearw/data/population/"
DATA_BASEPATH = "/Users/dd/pCloud Drive/data/population/"
# DATA_BASEPATH = "/home/dd/pCloudDrive/data/population/"

COUNTRY_PATH = 'data/country/'
GLOBAL_PATH = 'data/global/'
METADATA_PATH = 'data/metadata/'

COUNTRY_TEMPLATE = "{}_global_{}.csv"


# Gates foundation population data
BMGF = {'path': 'gatesfoundation/',
        'data': 
            {'files': 
                {'pop_data': 'IHME_POP_2017_2100_POP_BOTH_SEX_ALL_AGE_Y2020M05D01.csv'
                },
            'collections':
                {'global_pop': {
                    'basepath': 'IHME_POP_2017_2100_GLOBAL_{}.csv',
                    'vals': ['SLOWER', 'REFERENCE', 'FASTER', 'SDG']
                    },
                'country_pop': {
                    'basepath': 'IHME_POP_2017_2100_COUNTRY_{}.csv',
                    'vals': ['SLOWER', 'REFERENCE', 'FASTER', 'SDG']
                    }
                }
            }
}


# Wittgenstein Center population dataw
WITT2019 = {'path': 'wittgenstein-center-2019/',
        'data': 
            {'files': 
                {'recode': 'recode file.csv'},
            'collections':
                {'all_pop': {
                    'basepath': 'ssp{}epop_wide.csv',
                    'vals': range(1, 6)
                    },
                'global_pop': {
                    'basepath': 'ssp{}epop_global.csv',
                    'vals': range(1, 6)
                    },
                'country_pop': {
                    'basepath': 'ssp{}epop_country.csv',
                    'vals': range(1, 6)
                    }
                }
            }
        }

# Wittgenstein Center population dataw
WITT2023 = {'path': 'wittgenstein-center-2023/',
        'data': 
            {'files': 
                {'recode': 'recode file.csv'},
            'collections':
                {'all_pop': {
                    'basepath': 'ssp{}epop_wide.csv',
                    'vals': range(1, 6)
                    },
                'global_pop': {
                    'basepath': 'ssp{}epop_global.csv',
                    'vals': range(1, 6)
                    },
                'country_pop': {
                    'basepath': 'ssp{}epop_country.csv',
                    'vals': range(1, 6)
                    }
                }
            }
        }

# place for results
COMPUTED_DIRS = {'cleandata': 'clean/',
                'results': 'results/'
}

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
    return filepath.format(scenario)
    
# return the global path for a model+scenario combo
def get_global_path(model, scenario):
    filename = GLOBAL_TEMPLATE.format(model, scenario)
    return(DATA_BASEPATH + GLOBAL_PATH + filename)

def get_coll_vals(dataset, coll):
    ds = modelmgr.model_files(name)
    return(ds['data']['collections'][coll]['vals'])
