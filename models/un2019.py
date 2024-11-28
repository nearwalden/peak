# UN 2019 Projections

import modelmgr
import locations
import pandas as p
import numpy as np

# Dataset definition
UN2019 = {'path': 'un-wpp2019/',
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

#cols to drop
UN2019_DROPS = ['Variant', 'Notes', 'Country code', 'Type', 'Parent code']

# clean up the 2019 version
def un2019_global(basepath):
	ds = 'un_population_2019'
	scenarios = files.get_coll_vals(ds, 'all_pop')
	for scenario in scenarios:
		orig = p.read_csv(files.get_coll_file_path('source', ds, 'all_pop', scenario))
		out_path = files.get_coll_file_path('clean', ds, 'global_pop', scenario)
		# get global
		orig.drop(columns = UN2019_DROPS, inplace=True)
		world = orig[orig.Region == 'WORLD']
		new = world.drop(columns = 'Region').T
		new = new.reset_index()
		out = p.DataFrame()
		out['population'] = new[0].map(lambda x: int(x.replace(' ','')) * 1000)
		out['year'] = new['index']
		out['scenario'] = scenario
		out.to_csv(out_path)
		print("Wrote " + str(len(out)) + " records for " + scenario)
	return True

def un2019_countries():
	ds = 'un_population_2019'
	countries = locations.countries()    
	scenarios = files.get_coll_vals(ds, 'all_pop')
	for scenario in scenarios:
		orig = p.read_csv(files.get_coll_file_path(ds, 'all_pop', scenario))
		out_path = files.get_coll_file_path(ds, 'country_pop', scenario)
		# get global
		orig.drop(columns=UN2019_DROPS, inplace=True)
		out = p.DataFrame()
		first_country = True
		for country in countries:
			countrydf = orig[orig.Region == country].copy()
			new = countrydf.drop(columns='Region').T
			country_code = new.columns[0]
			new = new.reset_index()
			out[country] = new[country_code].map(lambda x: int(x.replace(' ','')) * 1000)
			if first_country:
				out['year'] = new['index']
			first_country = False
			out = out.copy()
		out['scenario'] = scenario
		out.to_csv(out_path)
		print("Wrote " + str(len(out)) + " records for " + scenario)
	return True
	
UN2019_MODEL = {'name': 'un2019',
				'create-global': un2019_global,
				'create-country': un2019_country,
				'files': UN2019}
	
modelmgr.register_model('un2019', UN2019_MODEL)