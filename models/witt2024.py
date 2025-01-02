# Wittgenstein 2024 Projections

import pandas as p
import numpy as np
import modelmgr
import files

# UN dataset 2022
WITT2024_PATH = 'wittgenstein-center-2024/wcde_data.csv'
WITT2024_SCENARIOS = ['SSP2', 'SSP1', 'SSP3', 'SSP4', 'SSP5', 'SSP2ZM', 'SSP2DM']

# columns to drop
#WITT2019_DROPS = ['Variant', 'Notes', 'Country code', 'Type', 'Parent code']
	
	
def witt2024_global(scenario):
	orig = p.read_csv(files.DATA_BASEPATH + WITT2024_PATH)
	# get global
	world = orig[orig.Area == "World"]
	worlds = world[world.Scenario == scenario]
	fit = np.polyfit(worlds.Year, worlds.Population, 2)
	outdf = p.DataFrame()
	outdf['year'] = np.arange(2020, 2101, 1)
	outdf['scenario'] = scenario
	out = []
	for year in range(2020, 2101, 1):
		pop = int((fit[0] * np.square(year) + fit[1] * year + fit[2]) * 1000)
		out.append(pop)
	outdf['population'] = out
	return(outdf)

def witt2024_country(scenario):
	orig = p.read_csv(files.DATA_BASEPATH + WITT2024_PATH)
	origs = orig[orig.Scenario == scenario]
	# get countries except world
	outdf = p.DataFrame()
	outdf['year'] = np.arange(2020, 2101, 1)
	outdf['scenario'] = scenario	
	for country in witt2024_country_names():
		country_pop = origs[origs.Area == country]
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
def witt2024_country_names():
	orig = p.read_csv(files.DATA_BASEPATH + WITT2024_PATH)
	# get countries except world
	countries = orig.Area.unique().tolist()
	countries.remove("World")
	return(countries)


WITT2024_MODEL = {'name': 'witt2024',
				'create-global': witt2024_global,
				'create-country': witt2024_country,
				'country-names': witt2024_country_names,
				'world-name': 'World',
				'scenarios': WITT2024_SCENARIOS}
		
modelmgr.register_model('witt2024', WITT2024_MODEL)