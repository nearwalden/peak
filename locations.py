# normalize locations

# from prefect import task, Flow
# from atlas import data
import pandas as p
import files


def bmgf_location_names ():
	df = p.read_csv (files.get_path ('bmgf_population', 'pop_data'))
	return df['location_name'].unique()
	

def witt_locations ():
	df = p.read_csv (files.get_path ('wittgenstein_centre_population', 'recode'))
	dfl = df[df['dim'] == 'isono'].copy()
	return dfl.drop('dim', axis=1)
	

def un_locations ():
	df = p.read_csv (files.get_path ('un_population', 'high_variant'))
	dfg = df.groupby('Region')
	outdf = p.DataFrame()
	outdf = dfg.first()
	outdf = outdf.reset_index()
	return outdf[outdf['Type'] == 'Country/Area'].copy()
	

def compare_names (names, dataset, un):
	not1 = []
	only1 = []
	both = []
	un_list = un['Region'].to_list()
	for item in names:
		if item in un_list:
			both.append (item)
		else:
			only1.append (item)
	for item in un_list:
		if item not in names:
			not1.append(item)
	out = {dataset: only1,
		'un': not1,
		'both': both
	}
	return out
	
def compare_numbers (witt, un):
	not1 = []
	only1 = []
	both = []
	un_list = un['Country code'].to_list()
	witt_list = wiit['code'].to_list()
	for item in witt_list:
		if item in un_list:
			both.append (item)
		else:
			only1.append (item)
	for item in un['Country code']:
		if item not in witt['code']:
			not1.append(item)
	out = {dataset: only1,
		'un': not1,
		'both': both
	}
	return out