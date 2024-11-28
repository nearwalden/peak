# UN 2022 Projections

import locations
import pandas as p
import numpy as np

# UN dataset 2022
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

# columns to drop
UN2022_DROPS = ['Variant', 'Notes', 'Location code', 'Type']


# global file
def un2022_global():
	ds = 'un_population_2022'
	scenarios = files.get_coll_vals(ds, 'all_pop')
	for scenario in scenarios:
		orig = p.read_csv(files.get_coll_file_path(ds, 'all_pop', scenario))
		out_path = files.get_coll_file_path(ds, 'global_pop', scenario)
		# get global
		world = orig[orig.Region == 'WORLD']
		out = p.DataFrame()
		out['population'] = world['population'].map(lambda x: int(x.replace(' ','')) * 1000)
		out['year'] = world['year']
		out['scenario'] = scenario
		out.to_csv(out_path)
		print("Wrote " + str(len(out)) + " records for " + scenario)
	return True

# country file
def un2022_countries():
	ds = 'un_population_2022'
	countries = locations.countries()    
	scenarios = files.get_coll_vals(ds, 'all_pop')
	for scenario in scenarios:
		orig = p.read_csv(files.get_coll_file_path(ds, 'all_pop', scenario))
		out_path = files.get_coll_file_path(ds, 'country_pop', scenario)
		out = p.DataFrame()
		first_country = True
		for country in countries:
			countrydf = orig[orig.Region == country].copy()
			out[country] = countrydf['population'].map(lambda x: int(x.replace(' ','')) * 1000).values
			if first_country:
				out['year'] = orig['year']
			first_country = False
			out = out.copy()
		out['scenario'] = scenario
		out.to_csv(out_path)
		print("Wrote " + str(len(out)) + " records for " + scenario)
	return True
