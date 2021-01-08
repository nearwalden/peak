# normalize locations

from prefect import flow
from atlas import data
import pandas as p

@flow
def bmgf_locations ():
	path = data.path('bmgf_population_2019_all', 'bmgf_population_2019')
	df = p.read_csv (path)
	dfg = df.groupby('location')
	return dfg['location_id'].first()
	
@flow 
def witt_locations ():
	
@flow
def un_locations ():
	
	
@flow
def report_bmgf (bmgf, un):
	
	
@flow
def report_witt (witt, un):
	
	






