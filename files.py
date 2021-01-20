# locations of everything

DATA_BASEPATH = "/mnt/c/Users/nearw/data/population/"


# Gates foundation population data
BMFG = {'path': 'gatesfoundation/',
        'basepath': DATA_BASEPATH,
        'data': 
            {'files': 
                {'pop_data': 'IHME_POP_2017_2100_POP_BOTH_SEX_ALL_AGE_Y2020M05D01.csv'}
            }
}

# Wittgenstein Center population dataw
WITT = {'path': 'wittgenstein-center/',
        'basepath': DATA_BASEPATH,
        'data': 
            {'files': 
                {'recode': 'recode file.csv'}
            }
}

# UN data 2019
UN = {'path': 'un-wpp2019/',
    'basepath': DATA_BASEPATH,
    'data': 
        {'files': 
            {'high_variant': 'WPP2019_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES_high.csv'}
        }
}

# place for results
RES = {'path': 'results/'}


DATASETS = {'bmgf_population': BMFG, 
            'wittgenstein_centre_population': WITT, 
            'un_population': UN,
            'results': RES}


def get_path (dataset, file):
    dataset = DATASETS[dataset]
    datasetpath = dataset['basepath'] + dataset['path']
    filepath = dataset['data']['files'][file]
    return datasetpath + filepath
