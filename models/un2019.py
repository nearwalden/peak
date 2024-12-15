# UN 2019 Projections

import modelmgr
import files
import pandas as p
# import numpy as np

# Dataset definition
UN2019_PATH = 'un-wpp2019/WPP2019_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES_{}.csv'
					
UN2019_SCENARIOS = ['high', 'medium', 'low']

#cols to drop
UN2019_DROPS = ['Variant', 'Notes', 'Country code', 'Type', 'Parent code']

# clean up the 2019 version
def un2019_global(scenario):
	orig = p.read_csv(files.get_scenario_file_path(UN2019_PATH, scenario))
	# get global
	orig.drop(columns = UN2019_DROPS, inplace=True)
	world = orig[orig.Region == 'WORLD']
	new = world.drop(columns = 'Region').T
	new = new.reset_index()
	out = p.DataFrame()
	out['population'] = new[0].map(lambda x: int(x.replace(' ','')) * 1000)
	out['year'] = new['index']
	out['scenario'] = scenario
	return out

# create a country file for one of the scenarios
def un2019_country(scenario, countries):
	orig = p.read_csv(files.get_scenario_file_path(UN2019_PATH, scenario))
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
	return out
	
def un2019_locations():
		df = p.read_csv(files.get_scenario_file_path(UN2019_FILEPATH, 'high'))
		dfg = df.groupby('Region')
		outdf = p.DataFrame()
		outdf = dfg.first()
		outdf = outdf.reset_index()
		return outdf   
	
def un2019_country_names():
	df = un2019_locations()
	return df[df.Type == 'Country/Area']['Region'].to_list()


def un2019_region_names():
	df = un2019_locations()
	return df[df.Type == 'Region']['Region'].to_list()


def un2019_subregion_names():
	df = un2019_locations()
	return df[df.Type == 'Subregion']['Region'].to_list()


UN2019_MODEL = {'name': 'un2019',
				'create-global': un2019_global,
				'create-country': un2019_country,
				'country-names': un2019_country_names,
				'world-name': 'WORLD',
				'scenarios': UN2019_SCENARIOS}
	
modelmgr.register_model('un2019', UN2019_MODEL)