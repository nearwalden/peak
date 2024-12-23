# UN 2022 Projections

import pandas as p
import modelmgr
import files

# UN dataset 2022
UN2022_PATH = 'un-wpp2022/WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1_POP_{}.csv'
UN2022_SCENARIOS = ['high', 'medium', 'low']

# columns to drop
UN2022_DROPS = ['Variant', 'Notes', 'Location code', 'Type']


# global file
def un2022_global(scenario):
	orig = p.read_csv(files.get_scenario_file_path(UN2022_PATH, scenario))
	# get global
	orig.drop(columns = UN2022_DROPS, inplace=True)
	world = orig[orig.Region == 'WORLD']
	out = p.DataFrame()
	out['population'] = world['population'].map(lambda x: int(x.replace(' ','')) * 1000)
	out['year'] = world['year']
	out['scenario'] = scenario
	return(out)

# country file
def un2022_country(scenario):
	orig = p.read_csv(files.get_scenario_file_path(UN2022_PATH, scenario))
	out = p.DataFrame()
	first_country = True
	for country in un2022_country_names():
		countrydf = orig[orig.Region == country].copy()
		out[country] = countrydf['population'].map(lambda x: int(x.replace(' ','')) * 1000).values
		if first_country:
			out['year'] = orig['year']
		first_country = False
		out = out.copy()
	out['scenario'] = scenario
	return(out)
	
def un2022_locations():
    df = p.read_csv(files.get_scenario_file_path(UN2022_PATH, 'high'))
    dfg = df.groupby('Region')
    outdf = p.DataFrame()
    outdf = dfg.first()
    outdf = outdf.reset_index()
    return(outdf)   #  outdf[outdf['Type'] == 'Country/Area'].copy()


def un2022_country_names():
    df = un2022_locations()
    return(df[df.Type == 'Country/Area']['Region'].to_list())


def un2022_region_names():
    df = un2022_locations()
    return(df[df.Type == 'Region']['Region'].to_list())


def un2022_subregion_names():
    df = un2022_locations()
    return(df[df.Type == 'Subregion']['Region'].to_list())

UN2022_MODEL = {'name': 'un2022',
				'create-global': un2022_global,
				'create-country': un2022_country,
				'country-names': un2022_country_names,
				'world-name': 'WORLD',
				'scenarios': UN2022_SCENARIOS}
	
modelmgr.register_model('un2022', UN2022_MODEL)
