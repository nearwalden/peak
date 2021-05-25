# locations of everything

DATA_BASEPATH = "/mnt/c/Users/nearw/data/population/"


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
WITT = {'path': 'wittgenstein-center/',
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
UN = {'path': 'un-wpp2019/',
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

# place for results
RES = {'path': 'results/'}


DATASETS = {'bmgf_population': BMGF, 
            'witt_population': WITT, 
            'un_population': UN,
            'results': RES}


def get_file_path(dataset, name):
    ds = DATASETS[dataset]
    datasetpath = ds['basepath'] + ds['path']
    filepath = ds['data']['files'][name]
    return datasetpath + filepath


def get_coll_file_path(dataset, coll, vals):
    ds = DATASETS[dataset]
    datasetpath = ds['basepath'] + ds['path']
    base_filepath = ds['data']['collections'][coll]['basepath']
    filepath = base_filepath.format(vals)
    return datasetpath + filepath


def get_coll_vals(dataset, coll):
    ds = DATASETS[dataset]
    return ds['data']['collections'][coll]['vals']
