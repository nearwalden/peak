# Wittgenstein 2015 Projections

import pandas as p
import numpy as np
import modelmgr
import files

# UN dataset 2022
WITT2015_PATH = 'wittgenstein-center-2015/wicdf_data.csv'
WITT2015_SCENARIOS = ['SSP2', 'SSP1', 'SSP3', 'SSP4', 'SSP5', 'SSP2-FT', 'SSP2-CER']
	
def witt2015_global(scenario):
	orig = p.read_csv(files.DATA_BASEPATH + WITT2015_PATH)
	# get global
	world = orig[orig.Area == "World"]
	fit = np.polyfit(world.Year, world.Population, 2)
	outdf = p.DataFrame()
	outdf['year'] = np.arange(2020, 2101, 1)
	outdf['scenario'] = scenario
	out = []
	for year in range(2020, 2101, 1):
		pop = int((fit[0] * np.square(year) + fit[1] * year + fit[2]) * 1000)
		out.append(pop)
	outdf['population'] = out
	return(outdf)

def witt2015_country(scenario):
	orig = p.read_csv(files.DATA_BASEPATH + WITT2015_PATH)
	# get countries except world
	outdf = p.DataFrame()
	outdf['year'] = np.arange(2020, 2101, 1)
	outdf['scenario'] = scenario	
	for country in witt2015_country_names():
		country_pop = orig[orig.Area == country]
		fit = np.polyfit(country_pop.Year, country_pop.Population, 2)
		out = []
		for year in range(2020, 2101):
			pop = int((fit[0] * np.square(year) + fit[1] * year + fit[2]) * 1000)
			out.append(pop)
		outdf[country] = out
		outdf = outdf.copy()
	return(outdf)
	
# locations for WITT
# currently not used.
def witt2015_country_names():
	orig = p.read_csv(files.DATA_BASEPATH + WITT2015_PATH)
	# get countries except world
	countries = orig.Area.unique().tolist()
	countries.remove("World")
	return(countries)


WITT2015_MODEL = {'name': 'witt2015',
				'create-global': witt2015_global,
				'create-country': witt2015_country,
				'country-names': witt2015_country_names,
				'world-name': 'World',
				'scenarios': WITT2015_SCENARIOS}
		
modelmgr.register_model('witt2015', WITT2015_MODEL)