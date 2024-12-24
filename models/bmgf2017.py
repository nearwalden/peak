# UN 2019 Projections

import pandas as p
import modelmgr
import files
# import numpy as np

# Dataset definition
BMGF2017_PATH = 'gatesfoundation/IHME_POP_2017_2100_POP_BOTH_SEX_ALL_AGE_Y2020M05D01.csv'
					
BMGF2017_SCENARIOS = ['SLOWER', 'REFERENCE', 'FASTER', 'SDG']

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
	'val': 'population',
	'location_name': 'location_name'
}

# return a new df with columns mapped
def mapdf(df, map):
	outdf = p.DataFrame()
	for key in map.keys():
		outdf[map[key]] = df[key]
	return outdf



def bmgf2017_global(scenario):
	orig = p.read_csv(files.DATA_BASEPATH + BMGF2017_PATH)
	# get global
	origg = orig[orig['location_id'] == 1]
	# start with 2020
	origg = origg[origg.year_id > 2019]
	# get right columns
	norm = mapdf(origg, BMGF_MAP)
	# do scenarios in order
	# pick out scenario
	norms = norm[norm['scenario_id'] == BMGF_SCENARIOS[scenario]].copy()
	norms['scenario'] = scenario
	norms['population'] = norms['population'].astype(int)
	return norms
	

def bmgf2017_country(scenario):
	orig = p.read_csv(files.DATA_BASEPATH + BMGF2017_PATH)
	# start with 2020
	orig = orig[orig.year_id > 2019]
	# get right columns
	norm = mapdf(orig, BMGF_MAP)
	# pick out scenario
	norms = norm[norm['scenario_id'] == BMGF_SCENARIOS[scenario]].copy()
	norms = norms.set_index('year')
	outdf = p.DataFrame()
	outdf['year'] = norms['year']
	for country in bmgf2017_location_names():
		normc = norms[norms['location_name'] == country]
		outdf[country] = normc['population'].astype(int)
	return(outdf.resest_index())
	
# locations for BMGF
def bmgf2017_location_names():
	df = p.read_csv(files.DATA_BASEPATH + BMGF2017_PATH)
	locations = df['location_name'].unique()
	locations.remove('Global')
	return(locations)

BMGF2017_MODEL = {'name': 'bmgf2017',
				'create-global': bmgf2017_global,
				'create-country': bmgf2017_country,
				'country-names': bmgf2017_location_names,
				'world-name': 'Global',
				'scenarios': BMGF2017_SCENARIOS}
	
modelmgr.register_model('bmgf2017', BMGF2017_MODEL)
