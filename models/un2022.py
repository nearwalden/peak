# UN 2022 Projections

import pandas as p
import modelmgr
import files

# UN dataset 2022
UN2022_PATH = 'WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1_POP_{}.csv'
UN2022_SCENARIOS = ['high', 'medium', 'low']

# columns to drop
UN2022_DROPS = ['Variant', 'Notes', 'Location code', 'Type']


# global file
def un2022_global(scenario):
	orig = p.read_csv(files.get_coll_file_path(ds, 'all_pop', scenario))
	out_path = files.get_coll_file_path(ds, 'global_pop', scenario)
	# get global
	world = orig[orig.Region == 'WORLD']
	out = p.DataFrame()
	out['population'] = world['population'].map(lambda x: int(x.replace(' ','')) * 1000)
	out['year'] = world['year']
	out['scenario'] = scenario
	return out

# country file
def un2022_country():
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

def un2022_locations():
    df = p.read_csv(files.get_coll_file_path('un_population_2022', 'all_pop', 'high'))
    dfg = df.groupby('Region')
    outdf = p.DataFrame()
    outdf = dfg.first()
    outdf = outdf.reset_index()
    return outdf   #  outdf[outdf['Type'] == 'Country/Area'].copy()


def un2022_country_names():
    df = un2022_locations()
    return df[df.Type == 'Country/Area']['Region'].to_list()


def un2022_region_names():
    df = un2022_locations()
    return df[df.Type == 'Region']['Region'].to_list()


def un2022_subregion_names():
    df = un2022_locations()
    return df[df.Type == 'Subregion']['Region'].to_list()

UN2022_MODEL = {'name': 'un2019',
				'create-global': un2022_global,
				'create-country': un2022_country,
				'country-names': un2022_country_names,
				'world-name': 'WORLD',
				'scenarios': UN2022_SCENARIOS}
	
modelmgr.register_model('un2022', UN2022_MODEL)
