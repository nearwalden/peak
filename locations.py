# normalize locations

from prefect import task, Flow
# from atlas import data
import pandas as p

BASE_PATH = "/Volumes/data/peak/population/"

BMGF_PATH = BASE_PATH + "gatesfoundation/IHME_POP_2017_2100_POP_BOTH_SEX_ALL_AGE_Y2020M05D01.csv"
WITT_RECODE = BASE_PATH + "wittgenstein-center/recode\ file.csv"
UN_PATH = BASE_PATH + "un-wpp2019/WPP2019_POP_F01_1_TOTAL_POPULATION_BOTH_SEXES_high.csv"

@task
def bmgf_locations ():
	# path = data.path('bmgf_population_2019_all', 'bmgf_population_2019')
	df = p.read_csv (BMGF_PATH)
	dfg = df.groupby('location_id')
	return dfg['location_name'].first()
	
@task 
def witt_locations ():
	# path = data.path('recode_file', 'witt_population')
	df = p.read_csv (WITT_RECODE)
	dfl = df[df['dim'] == 'isono'].copy()
	return dfl
	
@task
def un_locations ():
	# path = data.path('un_population_high_variant', 'un_population_estimate_2019')
	df = p.read_csv (UN_PATH)
	dfg = df.groupby ('Region')
	return dfg.first()
	
	
@task
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
	
with Flow("test") as test_flow:
	bmgf = bmgf_locations()
	print(bmgf)
	
with Flow("pop_locations") as flow:
	bmgf = bmgf_locations ()
	un = un_locations ()
	res = location_compare (bmgf['location_name'], un['Region'], 'bmgf', 'un')
	print (res)



