# locations of everything

# DATA_BASEPATH = "/mnt/c/Users/nearw/data/population/"
DATA_BASEPATH = "/Users/dd/pCloud Drive/data/population/"
# DATA_BASEPATH = "/home/dd/pCloudDrive/data/population/"


# Gates foundation population data
BMGF = {'path': 'gatesfoundation/',
        'basepath': DATA_BASEPATH,
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
        'basepath': DATA_BASEPATH,
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
        'basepath': DATA_BASEPATH,
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

# UN data 2019
UN2019 = {'path': 'un-wpp2019/',
    'basepath': DATA_BASEPATH,
    'data': 
        {'collections': 
            {'all_pop': {
                    'basepath': 'WPP2019_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES_{}.csv',
                    'vals': ['high', 'medium', 'low']},        
            'global_pop': {
                    'basepath': 'WPP2019_POP_GLOBAL_{}.csv',
                    'vals': ['high', 'medium', 'low']},
            'country_pop': {
                    'basepath': 'WPP2019_POP_COUNTRY_{}.csv',
                    'vals': ['high', 'medium', 'low']}
            }                  
        }
}

# UN data 2022
UN2022 = {'path': 'un-wpp2022/',
    'basepath': DATA_BASEPATH,
    'data': 
        {'collections': 
            {'all_pop': {
                    'basepath': 'WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1_POP_{}.csv',
                    'vals': ['high', 'medium', 'low']},        
            'global_pop': {
                    'basepath': 'WPP2022_POP_GLOBAL_{}.csv',
                    'vals': ['high', 'medium', 'low']},
            'country_pop': {
                    'basepath': 'WPP2022_POP_COUNTRY_{}.csv',
                    'vals': ['high', 'medium', 'low']}
            }                  
        }
}

# UN data 2024, files not fixed
UN2024 = {'path': 'un-wpp2024/',
    'basepath': DATA_BASEPATH,
    'data': 
        {'collections': 
            {'all_pop': {
                    'basepath': 'WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1_POP_{}.csv',
                    'vals': ['high', 'medium', 'low']},        
            'global_pop': {
                    'basepath': 'WPP2022_POP_GLOBAL_{}.csv',
                    'vals': ['high', 'medium', 'low']},
            'country_pop': {
                    'basepath': 'WPP2022_POP_COUNTRY_{}.csv',
                    'vals': ['high', 'medium', 'low']}
            }                  
        }
}

def get_val2(coll):
    
    

# clean datasets
CLEAN = {'path': 'cleandata/',
    'basepath': DATA_BASEPATH,
    'data': 
        {'collections': {
            'global': { 
                'basepath': '{}-global-{}',
                'val1': ['BMGF', 'WITT2019', 'WITT2023', 'UN2019', 'UN2022', 'UN2024'],
                'val2': {'BMGF': BMGF['data']['collections']['global_pop']['vals'],
            }
            }, 
            'country': {
                'basepath': '',
                'vals': ['BMGF', 'WITT2019', 'WITT2023', 'UN2019', 'UN2022', 'UN2024']
        }}}
    }


# place for results
RES = {'path': 'results/'}



DATASETS = {'bmgf_population': BMGF, 
            'witt_population_2019': WITT2019, 
            'witt_population_2023': WITT2023, 
            'un_population_2019': UN2019,
            'un_population_2022': UN2022,            
            'un_population_2024': UN2024,   
            'clean_data': CLEAN,         
            'results': RES}


def get_file_path(dataset, name):
    ds = DATASETS[dataset]
    datasetpath = ds['basepath'] + ds['path']
    filepath = ds['data']['files'][name]
    return datasetpath + filepath


def get_coll_file_path(dataset, coll, val):
    ds = DATASETS[dataset]
    datasetpath = ds['basepath'] + ds['path']
    base_filepath = ds['data']['collections'][coll]['basepath']
    filepath = base_filepath.format(val)
    return datasetpath + filepath
    
def get_coll_file_path2(dataset, coll, val1, val2):
    ds = DATASETS[dataset]
    datasetpath = ds['basepath'] + ds['path']
    base_filepath = ds['data']['collections'][coll]['basepath']
    filepath = base_filepath.format(val1, val2)
    return datasetpath + filepath


def get_coll_vals(dataset, coll):
    ds = DATASETS[dataset]
    return ds['data']['collections'][coll]['vals']
