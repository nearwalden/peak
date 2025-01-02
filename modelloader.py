# imports models 
# assumes package is 'models'

import importlib

MODEL_MODULE = "models"
	
def load_all():
	# importlib.import_module(MODEL_MODULE)
	__import__(MODEL_MODULE, fromlist=['*'])
	return True
	
def load_one(name):
	module = MODEL_MODULE + '.' + name
	importlib.import_module(module)
	return(name)
	
def reload_model(name):
	module = MODEL_MODULE + '.' + name
	importlib.reload(module)
	return(name)
	

	
	
