# manage models
import modelloader
import pandas as p

# Where the 

MODELS = {}

# called by model to register itself
def register_model(name, desc):
	MODELS[name] = desc
	return(name)

# returns the list of all model names	
def model_names():
	return(list(MODELS.keys()))

# calls the model loader for all models in the directory
def load_models():
	modelloader.load_all()
	return(model_names())

# loads a specific model
def load_model(name):
	modelloader.load_one(name)
	return(name)

# returns the list of all files for a specific model
def model_files(name):
	return(MODELS[name][files])

# creates clean data for global and country
def create_clean_data(model):
	scenarios = MODELS[model]['scenarios']
	for scenario in scenarios:
		data = MODELS[model]['create-global'](scenario)
		filename = files.get_global_path(model, scenario)
		data.write_csv(filename)
	return(True)
	
	
	

	
