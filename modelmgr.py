# manage models
import json
import pandas as p
import modelloader
import files

# Where the 

MODELS = {}

# called by model to register itself
def register_model(name, desc):
	MODELS[name] = desc
	return(name)

# returns the list of all model names	
def model_names():
	return(list(MODELS.keys()))
	
# writes modules to file
def write_loaded_models():
	filename = files.get_loaded_models_path()
	data = {'models': model_names()}
	with open(filename, "w", encoding='utf8') as fp:
		json.dump(data, fp, ensure_ascii = False) 
		
# read modules from file
def read_loaded_models():
	filename = files.get_loaded_models_path()
	with open(filename, "r", encoding ='utf8') as fp:
		return json.load(fp)['models']

# calls the model loader for all models in the directory
def load_models():
	modelloader.load_all()
	write_loaded_models()
	return(model_names())

# loads a specific model
def load_model(name):
	modelloader.load_one(name)
	write_loaded_models()
	return(name)
	
# reload modules
def reload_models():
	models = read_loaded_models()
	for name in models:
		modelloader.reload_model(name)
	return(models)
		

# returns the list of all files for a specific model
def model_files(name):
	return(MODELS[name][files])

# creates clean data for global and country
def create_clean_data(model):
	scenarios = MODELS[model]['scenarios']
	for scenario in scenarios:
		# global
		data = MODELS[model]['create-global'](scenario)
		filename = files.get_global_path(model, scenario)
		data.to_csv(filename)
		# country
		data = MODELS[model]['create-country'](scenario)
		filename = files.get_country_path(model, scenario)
		data.to_csv(filename)
	return(True)
	
	
	

	
