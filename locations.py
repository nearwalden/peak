# normalize locations

# from prefect import task, Flow
# from atlas import data
import pandas as p
import files


def bmgf_locations ():
	df = p.read_csv (files.get_path ('bmgf_population', 'pop_data'))
	dfg = df.groupby('location_id')
	return dfg['location_name'].first()
	

def witt_locations ():
	df = p.read_csv (files.get_path ('wittgenstein_centre_population', 'recode'))
	dfl = df[df['dim'] == 'isono'].copy()
	return dfl
	

def un_locations ():
	df = p.read_csv (files.get_path ('un_population', 'high_variant'))
	dfg = df.groupby ('Region')
	return dfg.first()
	

def location_compare (set1, set2, name1, name2):
	not1 = []
	only1 = []
	both = []
	for item in set1:
		if item in set2:
			both.append (item)
		else:
			only1.append (item)
	for item in set2:
		if item not in set1:
			not1.append(item)
	out = {name1: only1,
		name2: not1,
		'both': both
	}
	return out
	
