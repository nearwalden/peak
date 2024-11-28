# Routines to load in all global data and do lots of work on it

import files
import pandas as p

class World:
	# variables
	data = p.DataFrame()
	# load the data
	def __init__(self):
		bmgf_ds = 'bmgf_population'
		bmgf_coll = 'global_pop'
		for val in files.get_coll_vals(bmgf_ds, bmgf_coll):
			df = p.read_csv(files.get_coll_file_path(bmgf_ds, bmgf_coll, val))
			df = df.set_index('year')
			self.data['BMGF-' + val] = df['population']
		un2019_ds = 'un_population_2019'
		un2019_coll = 'global_pop'
		for val in files.get_coll_vals(un2019_ds, un2019_coll):
			df = p.read_csv(files.get_coll_file_path(un2019_ds, un2019_coll, val))
			df = df.set_index('year')
			self.data['UN2019-' + val] = df['population']
		un2022_ds = 'un_population_2022'
		un2022_coll = 'global_pop'
		for val in files.get_coll_vals(un2022_ds, un2022_coll):
			df = p.read_csv(files.get_coll_file_path(un2022_ds, un2022_coll, val))
			df = df.set_index('year')
			self.data['UN2022-' + val] = df['population']
		witt_ds = 'witt_population-2019'
		witt_coll = 'global_pop'
		for val in files.get_coll_vals(witt_ds, witt_coll):
			df = p.read_csv(files.get_coll_file_path(witt_ds, witt_coll, val))
			df = df.set_index('year')
			self.data['Witt-' + str(val)] = df['population']
	# return dataframe of stats for each model
	def compare_all(self, start=2022, end=2100):
		df = self.data[(self.data.index >= start) & (self.data.index <= end)]
		out = p.DataFrame()
		out['peak'] = df.max()
		out['peak_year'] = df.idxmax()
		out['manyears'] = df.sum()/1000000000
		out['mean'] = df.mean()
		return out
	# return a single year
	def year(self, yr):
		return self.data[self.data.index == yr]
	
	

