# Make clean files

import files
import pandas as p
import numpy as np

# All

GLOBAL_COLS = ['scenario', 'year', 'population']

# BMFG data cleaning

BMGF_SCENARIOS = {
    'SLOWER': -1,
    'REFERENCE': 0,
    'FASTER': 1,
    'SDG': 2
}

BMGF_MAP = {
    'scenario': 'scenario_id',
    'year_id': 'year',
    'val': 'population'
}


def bmgf_global():
    ds = 'bmgf_population'
    orig = p.read_csv(files.get_file_path(ds, 'pop_data'))
    # get global
    origg = orig[orig['location_id'] == 1]
    # start with 2020
    origg = origg[origg.year_id > 2019]
    # get right columns
    norm = mapdf(origg, BMGF_MAP)
    # do scenarios in order
    for scenario in BMGF_SCENARIOS.keys():
        out_path = files.get_coll_path(ds, 'global_pop', scenario)
        # pick out scenario
        norms = norm[norm['scenario_id'] == BMGF_SCENARIOS[scenario]].copy()
        norms['scenario'] = scenario
        norms['population'] = norms['population'].astype(int)
        norms.to_csv(out_path)
        print("Wrote " + str(len(norms)) + " records for " + scenario)
    return True


# UN data cleaning

UN_SCENARIOS = ['high', 'medium', 'low']

UN_DROPS = ['Variant', 'Notes', 'Country code', 'Type', 'Parent code']


def un_global():
    ds = 'un_population'
    scenarios = files.get_coll_vals(ds, 'all_pop')
    for scenario in scenarios:
        orig = p.read_csv(files.get_coll_file_path(ds, 'all_pop', scenario))
        out_path = files.get_coll_file_path(ds, 'global_pop', scenario)
        # get global
        orig = orig.drop(UN_DROPS, 1)
        world = orig[orig.Region == 'WORLD']
        new = world.drop('Region', 1).T
        new = new.reset_index()
        out = p.DataFrame()
        out['population'] = new[0].map(lambda x: int(x.replace(' ','')) * 1000)
        out['year'] = new['index']
        out['scenario'] = scenario
        out.to_csv(out_path)
        print("Wrote " + str(len(out)) + " records for " + scenario)
    return True

# Witt data cleaning

WITT_DROPS = ['Variant', 'Notes', 'Country code', 'Type', 'Parent code']


def witt_global():
    ds = 'witt_population'
    scenarios = files.get_coll_vals(ds, 'all_pop')
    age_drops = []
    for i in range(1, 22):
        age_drops.append('ageno_' + str(i))
    for scenario in scenarios:
        orig = p.read_csv(files.get_coll_file_path(ds, 'all_pop', scenario))
        out_path = files.get_coll_file_path(ds, 'global_pop', scenario)
        # get global
        orig = orig.drop(age_drops, 1)
        world = orig[(orig.eduno == 0) & (orig.sexno == 0) & (orig.isono == 900)]
        fit = np.polyfit(world.year, world.ageno_0, 2)
        out = []
        for year in range(2020, 2101):
            pop = (fit[0] * np.square(year) + fit[1] * year + fit[2]) * 1000
            out.append({
                'year': year,
                'scenario': scenario,
                'population': pop})
        outdf = p.DataFrame(out)
        outdf.to_csv(out_path)
        print("Wrote " + str(len(out)) + " records for " +str(scenario))
    return True


# utils


# return a new df with columns mapped
def mapdf(df, map):
    outdf = p.DataFrame()
    for key in map.keys():
        outdf[map[key]] = df[key]
    return outdf
