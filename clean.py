# Make clean files

import files
import pandas as p

### All

GLOBAL_COLS = ['scenario', 'year', 'population']

### BMFG data cleaning

BMFG_SCENARIOS = {
    'SLOWER': -1,
    'REFERENCE': 0,
    'FASTER': 1,
    'SDG': 2
}

BMFG_MAP = {
    'scenario_id': 'scenario',
    'year_id': 'year',
    'val': 'population'
}

def bmfg_global ():
    ds = 'bmgf_population'
    orig = p.read_csv (files.get_file_path (ds, 'pop_data'))
    norm = p.DataFrame()
    for col in BMFG_MAP.keys():
        norm[BMFG_MAP[col]] = orig[col]
    # get global
    origg = orig[orig['location_id'] == 1]
    # do scenarios in order
    for scenario in BMFG_SCENARIOS.keys():
        out_path = files.get_coll_path(ds, 'global_pop', scenario)
        # pick out scenario
        norms = norm[norm['scenario'] == BMFG_SCENARIOS[scenario]]
        norms.to_csv(out_path)
        print("Wrote " + str(len(origgs)) + " records for " + scenario)
    return True

### UN data cleaning

UN_MAP = {
    'scenario_id': 'scenario',
    'year_id': 'year',
    'val': 'population'
}

def un_global ():
    ds = 'un_population'
    orig = p.read_csv (files.get_file_path (ds, 'pop_data'))
    norm = p.DataFrame()
    for col in BMFG_MAP.keys():
        norm[BMFG_MAP[col]] = orig[col]
    # get global
    origg = orig[orig['location_id'] == 1]
    # do scenarios in order
    for scenario in BMFG_SCENARIOS.keys():
        out_path = files.get_coll_path(ds, 'global_pop', scenario)
        # pick out scenario
        norms = norm[norm['scenario'] == BMFG_SCENARIOS[scenario]]
        norms.to_csv(out_path)
        print("Wrote " + str(len(origgs)) + " records for " + scenario)
    return True
