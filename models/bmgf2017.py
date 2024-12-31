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
	origg = orig[orig.year_id > 2019]
	# get right columns
	norm = mapdf(origg, BMGF_MAP)
	norms = norm[norm['scenario_id'] == BMGF_SCENARIOS[scenario]].copy()
	out = p.DataFrame()
	first_country = True
	for country in bmgf2017_country_names():
		countrydf = norms[norms['location_name'] == country].copy()
		out[country] = countrydf['population'].astype(int).values
		if first_country:
			out['year'] = countrydf['year'].values
			out['scenario'] = scenario
		first_country = False
		out = out.copy()
	return(out)

BMGF2017_REGIONS = ['Global', 'Central Europe, Eastern Europe, and Central Asia',
   'Central Asia', 'Central Europe', 'Eastern Europe', 'High-income',
   'Australasia', 'High-income Asia Pacific',
   'High-income North America', 'Southern Latin America',
   'Western Europe', 'Latin America and Caribbean',
   'Andean Latin America', 'Caribbean', 'Central Latin America',
   'Tropical Latin America', 'North Africa and Middle East',
   'South Asia', 'Southeast Asia, East Asia, and Oceania',
   'East Asia', 'Oceania', 'Southeast Asia', 'Sub-Saharan Africa',
   'Central Sub-Saharan Africa', 'Eastern Sub-Saharan Africa',
   'Southern Sub-Saharan Africa', 'Western Sub-Saharan Africa']
	
# locations for BMGF
def bmgf2017_location_names():
	df = p.read_csv(files.DATA_BASEPATH + BMGF2017_PATH)
	locations = df['location_name'].unique().tolist()
	return(locations)
	
# countries
def bmgf2017_country_names():
	locations = bmgf2017_location_names()
	for name in BMGF2017_REGIONS:
		locations.remove(name)
	return(locations)

BMGF2017_MODEL = {'name': 'bmgf2017',
				'create-global': bmgf2017_global,
				'create-country': bmgf2017_country,
				'country-names': bmgf2017_country_names,
				'world-name': 'Global',
				'scenarios': BMGF2017_SCENARIOS}
	
modelmgr.register_model('bmgf2017', BMGF2017_MODEL)
