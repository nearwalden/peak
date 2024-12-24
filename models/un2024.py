# UN 2024 Projections

import pandas as p
import modelmgr
import files

# UN dataset 2022
UN2024_PATH = 'un-wpp2024/WPP2024_TotalPopulationBySex.csv'
UN2024_SCENARIOS = ['Medium', 'High', 'Low', 'Median PI', 'Upper 80 PI',
		'Lower 80 PI', 'Upper 95 PI', 'Lower 95 PI']
		# , 'Constant fertility',
	   	# 'Instant replacement', 'Zero migration', 'Constant mortality',
	   	# 'No change', 'Momentum', 'Instant replacement zero migration',
	   	# 'No fertility below age 18', 'Accelerated ABR decline',
	   	# 'Accelarated ABR decline w/rec.', ]

# columns to drop
UN2024_DROPS = ['SortOrder', 'LocID', 'Notes', 'ISO3_code', 'ISO2_code',
	'SDMX_code', 'LocTypeID', 'LocTypeName', 'ParentID', 'VarID',
	'MidPeriod', 'PopMale', 'PopFemale',	'PopDensity']


def un2024_global(scenario):
	orig = p.read_csv(files.DATA_BASEPATH + UN2024_PATH, low_memory=False)
	# get the scenario
	orig = orig[orig.Variant == scenario]
	# get global
	orig.drop(columns = UN2024_DROPS, inplace=True)
	world = orig[orig.Location == 'World']
	out = p.DataFrame()
	out['population'] = world['PopTotal'].map(lambda x: int(x * 1000))
	out['year'] = world['Time']
	out['scenario'] = scenario
	return(out)

# country file
def un2024_country(scenario):
	orig = p.read_csv(files.DATA_BASEPATH + UN2024_PATH, low_memory=False)
	out = p.DataFrame()
	first_country = True
	for country in un2024_country_names():
		countrydf = orig[orig.Location == country].copy()
		out[country] = countrydf['PopTotal'].map(lambda x: int(x * 1000)).values
		if first_country:
			out['year'] = orig['Time']
		first_country = False
		out = out.copy()
	out['scenario'] = scenario
	return(out)
	
def un2024_locations():
	df = p.read_csv(files.DATA_BASEPATH + UN2024_PATH, low_memory=False)
	dfg = df.groupby('Location')
	outdf = p.DataFrame()
	outdf = dfg.first()
	outdf = outdf.reset_index()
	return(outdf)   #  outdf[outdf['Type'] == 'Country/Area'].copy()


def un2024_country_names():
	df = un2024_locations()
	return(df[df.LocTypeName == 'Country/Area']['Location'].to_list())


def un2024_region_names():
	df = un2024_locations()
	return(df[df.LocTypeName == 'Region']['Location'].to_list())


def un2024_subregion_names():
	df = un2024_locations()
	return(df[df.LocTypeName == 'Subregion']['Location'].to_list())

UN2024_MODEL = {'name': 'un2024',
				'create-global': un2024_global,
				'create-country': un2024_country,
				'country-names': un2024_country_names,
				'world-name': 'World',
				'scenarios': UN2024_SCENARIOS}
		
modelmgr.register_model('un2024', UN2024_MODEL)